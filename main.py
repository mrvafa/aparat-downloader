import time

from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.parse 

BASE = 'https://www.aparat.com'
GECKODRIVER_PATH = '/home/mrvafa/Driver/geckodriver'
url = 'https://www.aparat.com/jadi/videos'

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
list_of_channel_videos = soup.find_all('div', attrs={'class':'item grid-item'})

video_link_page = []
for video_section in list_of_channel_videos:
    inner_div = video_section.find('div')
    inner_inner_div = inner_div.find('div')
    link = inner_inner_div.find('a')
    if 'href' in str(link):
        video_link_page.append(urllib.parse.urljoin(BASE, link['href']))

driver.close()
