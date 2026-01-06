"""
Runnable Selenium Python example that demonstrates robust XPath usage
with the local sample.html included in the examples/ folder.

Requirements:
  pip install selenium webdriver-manager
Usage:
  python code/selenium_example.py
"""

import os
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# Optional: use webdriver-manager for portability
try:
    from webdriver_manager.chrome import ChromeDriverManager
    CHROME_DRIVER = ChromeDriverManager().install()
except Exception:
    # Fallback: assume chromedriver is in PATH
    CHROME_DRIVER = "chromedriver"

def local_file_url(path: Path) -> str:
    return path.resolve().as_uri()

def find_and_print(driver, xpath, label):
    elems = driver.find_elements(By.XPATH, xpath)
    if not elems:
        print(f"[{label}] NOT FOUND: {xpath}")
        return
    for i, e in enumerate(elems, start=1):
        text = e.get_attribute("value") or e.text or "(no text/value)"
        tag = e.tag_name
        print(f"[{label}] {i}. <{tag}> -> {text}")

def main():
    base = Path(__file__).resolve().parents[1]  # project root
    demo = base / "examples" / "sample.html"
    if not demo.exists():
        print("ERROR: examples/sample.html not found. Clone repo and ensure file exists.")
        return

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # change if you want visible browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = ChromeService(CHROME_DRIVER) if isinstance(CHROME_DRIVER, str) else ChromeService(CHROME_DRIVER)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        url = local_file_url(demo)
        print("Opening:", url)
        driver.get(url)
        time.sleep(0.5)  # small wait for static file

        # 1: brittle absolute example (likely to fail in many pages)
        brittle_xpath = "//html/body/div[2]/div[1]/form/input[2]"
        find_and_print(driver, brittle_xpath, "brittle-absolute")

        # 2: anchor + axis (robust)
        anchor_xpath = "//label[normalize-space()='Username']/following-sibling::input[1]"
        find_and_print(driver, anchor_xpath, "anchor-following-sibling")

        # 3: partial dynamic id using starts-with
        startswith_xpath = "//input[starts-with(@id,'user_')]"
        find_and_print(driver, startswith_xpath, "starts-with-id")

        # 4: normalize-space on button
        btn_xpath = "//button[normalize-space()='Submit']"
        find_and_print(driver, btn_xpath, "normalize-button")

        # 5: combined conditions for Buy now
        buy_xpath = "//a[@role='button' and contains(@href,'/checkout') and normalize-space()='Buy now']"
        find_and_print(driver, buy_xpath, "combined-buy")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
