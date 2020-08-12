from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(
    executable_path="D:\Python_notebook\Drivers\geckodriver.exe")

driver.get("https://phptravels.org/clientarea.php")

user_ele = driver.find_element_by_name("username")

print(user_ele.is_displayed())  # returns true/falses based on element status
print(user_ele.is_enabled())  # returns true/false

pw_ele = driver.find_element_by_name("password")

print(pw_ele.is_displayed())  # returns true/falses based on element status
print(pw_ele.is_enabled())  # returns true/false

user_ele.send_keys("Kappa123@gmail.com")
pw_ele.send_keys("admin")

driver.find_element_by_xpath("//*[@id='login']").click()

time.sleep(5)
driver.close()
