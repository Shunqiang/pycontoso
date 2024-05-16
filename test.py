from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import json
driver = webdriver.Firefox()

driver.get("https://www.zhipin.com/job_detail/?query=&city=101020100&industry=&position=")

# title = driver.title
driver.implicitly_wait(10)
# data = json.loads(page_source)

# driver.implicitly_wait(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
text_box = driver.find_elements(By.CSS_SELECTOR,".job-name")
# text_box = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul li .job-name")))
# # submit_button = driver.find_element(by=By.ID, value="su")
print(text_box)
print(text_box)
for e in text_box:
    print(e.text)


# text_box.send_keys("周杰伦")

# submit_button.click()

# js_script = 'document.documentElement.scrollTop=10000'
# driver.execute_script(js_script)
# time.sleep(3)
# next = driver.find_element(by=By.XPATH, value="//a[contains(text(),'下一页 >')]")

# next.click()
# # time.sleep(3)
driver.quit()
