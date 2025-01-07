import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get(url='https://orteil.dashnet.org/cookieclicker/')

time.sleep(3)

accept= driver.find_element(By.CLASS_NAME,'cc_btn_accept_all')
select_lang= driver.find_element(By.ID,'langSelect-EN')

accept.click()
select_lang.click()

time.sleep(2)

click_cookie= driver.find_element(By.ID,'bigCookie')
for i in range(100):
    click_cookie.click()


# input('enter')
time.sleep(3)