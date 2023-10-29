#  script to bypass 2captcha

# import twocaptcha
import selenium
from PIL import Image
import pytesseract
from selenium.webdriver.common.by import By
# from twocaptcha import TwoCaptcha
from selenium import webdriver
import time
import os


from selenium import webdriver

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = "/usr/bin/google-chrome" 
# driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome(executable_path="/usr/bin/google-chrome")


# def bypass_recaptcha(driver, site_key):
#     #  bypass recaptcha
#     driver.get("https://2captcha.com/demo/recaptcha-v3-invisible")

def bypass_recaptcha():
    #  bypass recaptcha
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    # driver = webdriver.PhantomJS()
    
    # wait for 10 seconds
    # driver.implicitly_wait(10)

    # driver.get("https://captcha.com/demos/features/captcha-demo.aspx")
    driver.get("https://www.orangehrm.com/30-day-free-trial")
    iframe_element = driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")
    driver.switch_to.frame(iframe_element)
    
    driver.implicitly_wait(5)

    # get dom element in driver.find_element
    # https://stackoverflow.com/questions/5986800/how-to-get-dom-element-in-selenium-webdriver-using-python

    checkbox_element = driver.find_element(By.CSS_SELECTOR, '[class="recaptcha-checkbox-border"]')
    checkbox_element.click()
    time.sleep(20)
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//input[@id='sitekey']").send_keys(site_key)
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()


bypass_recaptcha()
