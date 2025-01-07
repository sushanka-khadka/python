import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver_path= r'D:\learn\Development\chromedriver-win64\chromedriver.exe'
service= Service(executable_path=driver_path)
driver= webdriver.Chrome(service=service)
driver.get(url='https://secure-retreat-92358.herokuapp.com')

f_name= driver.find_element(By.NAME,'fName')
l_name= driver.find_element(By.NAME,'lName')
email= driver.find_element(By.NAME,'email')
submit= driver.find_element(By.CLASS_NAME,'btn-block')

f_name.send_keys('john')
l_name.send_keys('agustin')
email.send_keys('test@me.com')

time.sleep(2)
submit.click()

input('press enter to quit')
driver.quit()