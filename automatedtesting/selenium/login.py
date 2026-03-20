#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

URL = "https://www.saucedemo.com/"

def login(user, password):
    print("Starting the browser...")
    options = ChromeOptions()
    options.add_argument("--headless=new")  # Headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)  # Selenium manager will pick the correct chromedriver
    print("Browser started successfully. Navigating to the demo page to login.")
    driver.get(URL)

    # Perform login
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    print("Login successful.")
    return driver


def add_items(driver):
    print("Start test adding items to cart...")
    items = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
    added_items = []

    for item in items[:min(6, len(items))]:
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        #print(item_name)
        button = item.find_element(By.CSS_SELECTOR, ".pricebar > button")
        button.click()
        added_items.append(item_name)

    print("Items '{}' added.".format("', '".join(added_items)))

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    cart_items_count = int(cart_badge.text)
    assert len(added_items) == cart_items_count, "Cart count mismatch!"
    print("Items added successfully!")


def remove_items(driver):
    print("Start test removing items from the cart...")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    items = driver.find_elements(By.CLASS_NAME, "cart_item")
    removed_items = []

    for item in items:
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        button = item.find_element(By.CSS_SELECTOR, ".item_pricebar > button")
        button.click()
        removed_items.append(item_name)

    print("Items '{}' removed.".format("', '".join(removed_items)))

    try:
        driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        raise AssertionError("Cart is not empty!")
    except NoSuchElementException:
        print("All items removed successfully!")


if __name__ == "__main__":
    driver = login("standard_user", "secret_sauce")
    add_items(driver)
    remove_items(driver)
    driver.quit()
    print("UI Tests completed successfully!")
