import undetected_chromedriver as uc
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent

# Generate a random user agent
ua = UserAgent()
user_agent = ua.chrome

# Set up the undetected Chrome driver options
options = uc.ChromeOptions()
options.add_argument(f'--user-agent={user_agent}')  # Apply randomized user agent
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = uc.Chrome(options=options)

driver.set_window_size(1024, 768)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


try:
    # Navigate to the website
    driver.get('https://www.browserscan.net/bot-detection')

    # Random delay to mimic human interaction; adjust as needed
    time.sleep(50)

    # Find an element and print its text
    element = driver.find_element(By.TAG_NAME, 'a')
    print(f'Page title is: {element.text}')

finally:
    # Close the browser
    driver.quit()
