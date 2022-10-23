from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_drver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    drver = webdriver.Chrome(options=options)
    drver.get("http://automated.pythonanywhere.com")

    return drver

def main():
    driver = get_drver()
    element = driver.find_element('xpath', '/html/body/div[1]/div/h1[1]')
    return element.text

print(main())