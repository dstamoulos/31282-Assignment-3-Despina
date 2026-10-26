from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

# SCENARIO 1 - Add MacBook to cart
driver.get("https://opencart.abstracta.us/")
time.sleep(2)

macbook = driver.find_element(
    By.XPATH,
    "//h4/a[text()='MacBook']/ancestor::div[contains(@class,'product-thumb')]"
)

add_to_cart = macbook.find_element(
    By.XPATH,
    ".//button[contains(@onclick,'cart.add')]"
)

add_to_cart.click()
time.sleep(2)
driver.get(
    "https://opencart.abstracta.us/index.php?route=checkout/cart"
)

time.sleep(2)
if "MacBook" in driver.page_source:
    print("Scenario 1: PASS - MacBook was added to the shopping cart")
else:
    print("Scenario 1: FAIL - MacBook was not found in the shopping cart")

# SCENARIO 2 - Change quantity to 2
quantity_box = driver.find_element(
    By.XPATH,
    "//input[contains(@name,'quantity')]"
)
quantity_box.clear()
quantity_box.send_keys("2")

update_button = driver.find_element(
    By.XPATH,
    "//button[@data-original-title='Update']"
)

update_button.click()
time.sleep(3)
quantity_box = driver.find_element(
    By.XPATH,
    "//input[contains(@name,'quantity')]"
)

if quantity_box.get_attribute("value") == "2":
    print("Scenario 2: PASS - Quantity updated from 1 to 2")
else:
    print("Scenario 2: FAIL - Quantity did not update to 2")

# SCENARIO 3 - Remove MacBook
remove_button = driver.find_element(
    By.XPATH,
    "//button[@data-original-title='Remove']"
)
remove_button.click()

time.sleep(3)

if "MacBook" not in driver.page_source:
    print("Scenario 3: PASS - MacBook was removed from the shopping cart")
else:
    print("Scenario 3: FAIL - MacBook is still in the shopping cart")

time.sleep(3)
driver.quit()