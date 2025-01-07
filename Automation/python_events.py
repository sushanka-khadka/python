from selenium import webdriver
from selenium.webdriver.common.by import By
from sqlalchemy.sql.visitors import iterate

driver= webdriver.Chrome()
driver.get('https://www.python.org')


event_dates= driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
event_names= driver.find_elements(By.CSS_SELECTOR,'div.event-widget ul.menu a')

for date,event in zip(event_dates,event_names):
    print(date.text,event.text)

events= {}
for index,date in enumerate(event_dates):
    events[index]={
        'date': date.text,
        'event': event_names[index].text
    }


print('-'*50)
print(events)

