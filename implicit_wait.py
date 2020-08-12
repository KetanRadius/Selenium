from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(
    executable_path="D:\Python_notebook\Drivers\geckodriver.exe")

driver.get("https://phptravels.org/clientarea.php")  # opening url takes timne

driver.implicitly_wait(10)  # seconds

assert "Client Area - PHPTRAVELS" in driver.title  # this will return true/false

driver.find_element_by_name("username").send_keys("admin@gmail.com")
driver.find_element_by_name("password").send_keys("admin")

driver.find_element_by_xpath("//*[@id='login']").click()

driver.close()
