
import requests

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import undetected_chromedriver as uc


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}


def cardkingdom_price(card_name_url):
    url = "https://json.edhrec.com/cards/"

    transformed_url = requests.get(card_name_url, headers=headers).url
    card_name = transformed_url.split("/")[-1]
    try:
        response = requests.get(url + card_name, headers=headers)
        data = response.json()
        price = data["prices"]["cardkingdom"]["price"]
    except Exception:
        price = "N/A"

    sleep(0.5)
    return price


def tcgplayer_price(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument(f"user-agent={headers['User-Agent']}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    price_element = WebDriverWait(driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//span[contains(@class, "spotlight__price")]')))

    sleep(10)
    price = price_element.text
    driver.quit()
    if price:
        price = price.replace("$", "") + "$"
    else:
        price = "N/A"

    return price


def cardmarket_price(url):
    options = uc.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")

    driver = uc.Chrome(options=options)
    driver.get(url)

    sleep(5)
    # driver.save_screenshot("screenshot.png")
    cookie_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
    cookie_button.click()
    sleep(2)

    try:
        data = driver.find_elements(By.TAG_NAME, "dd")[3:7]

        if data[0].text.isnumeric():
            info = dict(zip(["available_items", "lowest_price", "price_trend"], [x.text for x in data[:-1]]))
        else:
            info = dict(zip(["available_items", "lowest_price", "price_trend"], [x.text for x in data[1:]]))
    except IndexError:
        info = {"available_items": "N/A", "lowest_price": "N/A", "price_trend": "N/A"}

    driver.quit()

    return info
