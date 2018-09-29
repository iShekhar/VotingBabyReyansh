from time import sleep
from appium.webdriver import webdriver

chrome_driver = webdriver.webdriver.Chrome()

chrome_driver.get(
    'https://mycutebaby.in/contest/participant/?n=5bab549a8965d&utm_source=wsapp_share&utm_campaign=September_2018&utm_medium=shared&utm_term=wsapp_shared_5bab549a8965d&utm_content=participant')
# Notification pop-up
sleep(10)
chrome_driver.find_element_by_xpath('//*[@id="onesignal-popover-cancel-button"]').click()
# Accept cookies pop-up
chrome_driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div/div[4]/button').click()
# FB-close pop-up
# sleep(5)
# chrome_driver.find_element_by_id('fb-close').click()
# Enter name
chrome_driver.find_element_by_id('v').send_keys('Shekhar')
# Vote
chrome_driver.find_element_by_xpath('//*[@id="vote_btn"]/span[2]').click()
chrome_driver.close()