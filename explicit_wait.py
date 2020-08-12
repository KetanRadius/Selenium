from selenium import webdriver
import time
driver = webdriver.Firefox(
    executable_path="D:\Python_notebook\Drivers\geckodriver.exe")

driver.maximize_window()

driver.get("https://www.expedia.com/")

time.sleep(5)

# click on flights button
driver.find_element_by_xpath(
    "//*[@id='uitk-tabs-button-container']/li[2]/a").click()

time.sleep(2)

driver.find_element_by_xpath(
    "//*[@id='wizard-flight-tab-roundtrip']/div/div[1]/div/div[1]/div/div/div/button").click()

time.sleep(2)

driver.find_element_by_name("Where are you leaving from?").send_keys("SYO")
print(driver.title)
print(driver.current_url)
time.sleep(3)

driver.close()
