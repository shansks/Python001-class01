from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://shimo.im/welcome")
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button').click()
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('18251894789')
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('1994shj')
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
time.sleep(3)
driver.quit()