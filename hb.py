from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver = '.\chromedriver.exe' #location of chrome webdriver

browser = webdriver.Chrome(chromedriver)
browser.get('http://hostellogin.srmuniv.ac.in/srmclb/')

url1 = browser.current_url
url2 = url1

while url1 == url2:
    username = browser.find_element_by_name('accountname')
    username.send_keys('RA1611003010585') #username

    username = browser.find_element_by_name('password')
    username.send_keys('password') #password

    browser.execute_script("loginform()")
    url2 = browser.current_url
    




