from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="wd")
submit_button = driver.find_element(by=By.ID, value="su")


text_box.send_keys("周杰伦")

submit_button.click()

js_script = 'document.documentElement.scrollTop=10000'
driver.execute_script(js_script)
time.sleep(3)
next = driver.find_element(by=By.XPATH, value="//a[contains(text(),'下一页 >')]")

next.click()
time.sleep(3)
driver.quit()