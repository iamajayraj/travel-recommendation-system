import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("C:/Users/iamaj/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=s)
time.sleep(5)

def destination_html(destination):
    driver.get('https://holidayz.makemytrip.com/holidays/india/search?dest={}'.format(destination))
    time.sleep(10)
    old_height = driver.execute_script('return document.body.scrollHeight')

    time.sleep(10)
    counter = 1

    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(10)

        new_height = driver.execute_script('return document.body.scrollHeight')

        print(new_height)
        print(old_height)
        print(counter)
        counter+=1

        if new_height==old_height:
            break

        old_height = new_height

    time.sleep(30)

    html = driver.page_source

    with open(destination+'.html', 'w', encoding='utf-8') as f:
        f.write(html)

    time.sleep(60)


destinations = ['Maharashtra',"Goa","Rajasthan","Andaman",'Kerala','Kashmir','Himachal%20Pradesh','South%20India','North%20East','Ladakh','Gujarat', 'Uttarakhand']

for destination in destinations:
    destination_html(destination)