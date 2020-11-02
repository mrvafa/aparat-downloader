import time

from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.parse
import requests

BASE = 'https://www.aparat.com'
GECKODRIVER_PATH = '/home/mrvafa/Driver/geckodriver'
url = 'https://www.aparat.com/jadi/videos'


def get_download_link_from_video_page(video_page_url):
    res = requests.get(video_page_url)
    if res.status_code == 200:
        video_page_soup = BeautifulSoup(res.text, 'html.parser')
        span_download_links = video_page_soup.find_all('li', attrs={'class': 'menu-item-link link'})
        a_download_link = span_download_links[len(span_download_links) - 1].find('a')
        if 'href' in str(a_download_link):
            return a_download_link['href']

    else:
        print(f'Error while getting {video_page_url} {res.text}')


driver = webdriver.Firefox(executable_path=GECKODRIVER_PATH)
driver.get(url)

# Scroll to end of file
lenOfPage = driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while not match:
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True

js_script_get_html_code = 'return (document.documentElement.outerHTML);'
html_output = driver.execute_script(js_script_get_html_code)

# Get video page links
soup = BeautifulSoup(html_output, 'html.parser')
list_of_channel_videos = soup.find_all('div', attrs={'class': 'item grid-item'})

video_link_pages = []
for video_section in list_of_channel_videos:
    inner_div = video_section.find('div')
    inner_inner_div = inner_div.find('div')
    link = inner_inner_div.find('a')
    if 'href' in str(link):
        video_link_pages.append(urllib.parse.urljoin(BASE, link['href']))

links = []
for video_link_page in video_link_pages:
    link = get_download_link_from_video_page(video_link_page)
    if link:
        links.append(link)

with open('links.json', 'w') as f:
    if links:
        json.dump(links, f)

driver.close()
