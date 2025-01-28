from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def main():
    options = Options()

    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)

    try:
        driver.execute_script("window.console.debug = function() {};")

        driver.get("https://www.browserscan.net/bot-detection")

        driver.execute_script("console.debug = function() {};")


        driver.refresh()

        time.sleep(300)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
