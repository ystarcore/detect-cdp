import undetected_chromedriver as uc
import time
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.chrome

options = uc.ChromeOptions()
options.add_argument(f"--user-agent={user_agent}")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
driver = uc.Chrome(options=options)

# Execute script to modify the webdriver property
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
    """
    },
)

driver.get("https://www.browserscan.net/bot-detection")

time.sleep(50)

driver.quit()
