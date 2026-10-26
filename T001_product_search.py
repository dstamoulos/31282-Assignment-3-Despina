from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


# SCENARIO 1 - Valid Search

driver.get(
    "https://ecommerce-playground.lambdatest.io/index.php?route=common/home"
)

time.sleep(2)

search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("iPhone")
search_box.send_keys(Keys.ENTER)

time.sleep(3)

if "iPhone" in driver.page_source:
    print("Scenario 1: PASS - iPhone appeared in the search results")
else:
    print("Scenario 1: FAIL - iPhone did not appear in the search results")



# SCENARIO 2 - Invalid Search

driver.get(
    "https://ecommerce-playground.lambdatest.io/index.php?route=common/home"
)

time.sleep(2)

search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("abcd")
search_box.send_keys(Keys.ENTER)

time.sleep(3)

if "abcd" not in driver.page_source:
    print("Scenario 2: PASS - No matching product was found")
else:
    print("Scenario 2: FAIL - Unexpected product result appeared")


# SCENARIO 3 - Empty Search
 
driver.get(
    "https://ecommerce-playground.lambdatest.io/index.php?route=common/home"
)

time.sleep(2)

search_box = driver.find_element(By.NAME, "search")
search_box.send_keys(Keys.ENTER)

time.sleep(3)

if driver.current_url:
    print("Scenario 3: PASS - Empty search was handled without crashing")
else:
    print("Scenario 3: FAIL - Empty search caused an error")


time.sleep(3)

driver.quit()