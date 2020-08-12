from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(
    executable_path="D:\Python_notebook\Drivers\geckodriver.exe")

driver.get("https://www.spicejet.com/")

print(driver.title)

driver.get("http://www.pavantestingtools.com/")

time.sleep(5)  # sleep for 5 seconds

print(driver.title)

driver.back()   # goes back to the previous page
time.sleep(5)

print(driver.title)

driver.forward()  # goes to the next page

time.sleep(5)
print(driver.title)

driver.quit()
