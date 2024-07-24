import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import csv


def form_submit():

    #logging.basicConfig(level=logging.DEBUG)

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')


    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        url = "https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform"
        driver.get(url)
      
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))

        time.sleep(5)

        input_elements = driver.find_elements(By.CLASS_NAME, 'whsOnd.zHQkBf')

        file = open("data.csv")
        csvreader = csv.reader(file, delimiter=',')
        for row in csvreader:
            inputs = [row[0], row[1], row[2], row[4], row[5], row[6], row[7]]
            address_input_value = row[3]
         
        for i in range(7):
            input_elements[i].clear()
            input_elements[i].send_keys(inputs[i])
        
        address_input = driver.find_element(By.CLASS_NAME, 'KHxj8b.tL9Q4c')
        address_input.clear()
        address_input.send_keys(address_input_value)

        time.sleep(10)  # Keep the browser open for 30 seconds for debugging

        submit_element = driver.find_element(By.CLASS_NAME, 'NPEfkd.RveJvd.snByac')
        submit_element.click()

        time.sleep(5) # For confirmation page

        screenshot_path = './screenshots/confirmation_page.png'
        driver.save_screenshot(screenshot_path)
 
    finally:
        driver.quit()

    return screenshot_path
    

if __name__ == "__main__":
    screenshot_path = form_submit()
    print("Screenshot saved to", screenshot_path)