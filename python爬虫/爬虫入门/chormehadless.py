from selenium import webdriver

#chrome_driver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver)

# chrome_options.add_argument('--disable-gpu')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.baidu.com")
print(driver.current_url)

driver.find_element_by_id("kw").send_keys("iphone")
driver.find_element_by_id("su").click()
source = driver.page_source #

print(source)

driver.quit()