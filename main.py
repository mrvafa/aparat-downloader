import time

from selenium import webdriver

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



driver.close()
