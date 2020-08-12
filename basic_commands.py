from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox(
    executable_path="D:\Python_notebook\Drivers\geckodriver.exe")

driver.get("http://www.facebook.com/")

print(driver.title)  # Title of the page

print(driver.current_url)  # Returns Url of the page

time.sleep(3)

driver.find_element_by_xpath(
    "//*[@id='loginbutton']").click()

time.sleep(5)

print(driver.title)
print(driver.current_url)

driver.close()  # close the browser
driver.quit()   # closes all the browsers
