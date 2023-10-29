import undetected_chromedriver as uc
from apify_client import ApifyClient
import time

web = "https://www.google.com/recaptcha/api2/demo"
options = uc.ChromeOptions()
options.headless = False
    # client = ApifyClient()
    # page = client.actor("xhxhxhxh/apify-web-scraper").call(input={"url": web})


driver = uc.Chrome(options=options, version_main=112)

try: 
    driver.get(web)
    # find sitekey by id
    # sitekey = driver.find_element(By.ID, "recaptcha-anchor").get_attribute("data-sitekey")
    
    sitekey = driver.find_element(by='id', value='recaptcha-demo').get_attribute('data-sitekey')

    # initialise ApifyClient
    api_key = "apify_api_XqWkV0SZYLl66JgoORFdLTfynvKoZ83HRJXJ"
    client = ApifyClient(api_key)

    ANTI_CAPTCHA_KEY = "c5fd717ea980d6487e705a13f6a7c8e5"
    PROTECTED_WEBSITE_URL = "https://www.google.com/recaptcha/api2/demo"
    CAPTCHA_DATA_SITEKEY = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"

    run_input = {
    "key": ANTI_CAPTCHA_KEY,
    "webUrl": PROTECTED_WEBSITE_URL,
    "siteKey": CAPTCHA_DATA_SITEKEY
    }

    run = client.actor("petr_cermak/anti-captcha-recaptcha").call(run_input=run_input)


    gCaptchaResponse = client.actor("petr_cermak/anti-captcha-recaptcha").last_run().key_value_store().get_record(key="OUTPUT").get('value')
    print(gCaptchaResponse)

    driver.execute_script("document.getElementById('g-recaptcha-response').value = '{}';".format(gCaptchaResponse))
    driver.find_element(by='xpath', value='//*[@id="recaptcha-demo-submit"]').click()
    time.sleep(3)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
    