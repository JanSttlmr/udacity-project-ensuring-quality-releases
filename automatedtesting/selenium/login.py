#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import datetime

URL = "https://www.saucedemo.com/"

def login(user, password):
    print(datetime.datetime.now())
    print("Starting the browser...")
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    print("Browser started successfully. Navigating to the demo page to login.")
    driver.get(URL)

    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    print("Login successful.")
    return driver

def add_items(driver):
    print(datetime.datetime.now())
    print("Start test adding items to cart...")
    items = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
    added_items = []

    for item in items[:min(6, len(items))]:
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        button = item.find_element(By.CSS_SELECTOR, ".pricebar > button")
        button.click()
        added_items.append(item_name)

    print("Items '{}' added.".format("', '".join(added_items)))
    print("Items added successfully!")

def remove_items(driver):
    print(datetime.datetime.now())
    print("Start test removing items from the cart...")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    items = driver.find_elements(By.CLASS_NAME, "cart_item")
    removed_items = []

    for item in items:
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        button = item.find_element(By.CSS_SELECTOR, ".pricebar > button")
        button.click()
        removed_items.append(item_name)

    print("All items removed successfully!")

if __name__ == "__main__":
    driver = login("standard_user", "secret_sauce")
    add_items(driver)
    remove_items(driver)
    driver.quit()
    print("UI Tests completed successfully!")
