from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
inp = driver.find_element_by_id("kw")
inp.send_keys("孟小帅")
button = driver.find_element_by_id("su")
button.click()

