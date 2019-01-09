from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get('http://orteil.dashnet.org/cookieclicker/')
time.sleep(1)

cookie = browser.find_element_by_id('bigCookie')

product0 = browser.find_element_by_id('product0')
product1 = browser.find_element_by_id('product1')
product2 = browser.find_element_by_id('product2')
product3 = browser.find_element_by_id('product3')

while True:
    cookie.click()
    try:
        product0.click()
        product1.click()
        product2.click()
        product3.click()
    except:
        pass

browser.quit()

