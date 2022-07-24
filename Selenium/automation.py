from selenium import webdriver

chrome_browser=webdriver.Chrome('./chromedriver.exe')

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
chrome_browser.maximize_window()
user_message=chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('i am cool')

chrome_browser.quit()