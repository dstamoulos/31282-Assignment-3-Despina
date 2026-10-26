from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

# SCENARIO 1 - Add MacBook to Wish List
driver.get(
    "https://opencart.abstracta.us/index.php?route=account/login"
)

time.sleep(2)
email_box = driver.find_element(By.NAME, "email")
email_box.send_keys("dtest@gmail.com")

password_box = driver.find_element(By.NAME, "password")
password_box.send_keys("dtest")

login_button = driver.find_element(
    By.XPATH,
    "//input[@value='Login']"
)

login_button.click()
time.sleep(3)
driver.get("https://opencart.abstracta.us/")
time.sleep(2)

macbook = driver.find_element(
    By.XPATH,
    "//h4/a[text()='MacBook']/ancestor::div[contains(@class,'product-thumb')]"
)

wishlist_button = macbook.find_element(
    By.XPATH,
    ".//button[contains(@onclick,'wishlist.add')]"
)

wishlist_button.click()
time.sleep(2)

driver.get(
    "https://opencart.abstracta.us/index.php?route=account/wishlist"
)

time.sleep(2)

if "MacBook" in driver.page_source:
    print("Scenario 1: PASS - MacBook was added to the wish list")
else:
    print("Scenario 1: FAIL - MacBook was not found in the wish list")

# SCENARIO 2 - Add Canon EOS 5D
driver.get("https://opencart.abstracta.us/")
time.sleep(2)

canon = driver.find_element(
    By.XPATH,
    "//h4/a[text()='Canon EOS 5D']/ancestor::div[contains(@class,'product-thumb')]"
)

wishlist_button_2 = canon.find_element(
    By.XPATH,
    ".//button[contains(@onclick,'wishlist.add')]"
)

wishlist_button_2.click()
time.sleep(2)

driver.get(
    "https://opencart.abstracta.us/index.php?route=account/wishlist"
)

time.sleep(2)

page = driver.page_source

if "MacBook" in page and "Canon EOS 5D" in page:
    print("Scenario 2: PASS - Both products appeared in the wish list")
else:
    print("Scenario 2: FAIL - One or both products were missing")

# SCENARIO 3 - Remove MacBook
macbook_row = driver.find_element(
    By.XPATH,
    "//a[text()='MacBook']/ancestor::tr"
)

remove_button = macbook_row.find_element(
    By.XPATH,
    ".//a[contains(@href,'remove')]"
)

remove_button.click()
time.sleep(3)
page = driver.page_source

if "MacBook" not in page and "Canon EOS 5D" in page:
    print("Scenario 3: PASS - MacBook was removed and Canon EOS 5D remained")
else:
    print("Scenario 3: FAIL - Wish list did not update as expected")

time.sleep(3)
driver.quit()