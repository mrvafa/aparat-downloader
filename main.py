from selenium import webdriver

GECKODRIVER_PATH = '/home/mrvafa/Driver/geckodriver'
url = 'https://www.aparat.com/jadi/videos'

driver = webdriver.Firefox(executable_path=GECKODRIVER_PATH)
driver.get(url)
