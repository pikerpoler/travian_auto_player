from selenium import webdriver
from time import sleep

def login(email, password, low_resolution=True):
    login_xpaths = {'username_field': '//*[@id="content"]/div[1]/div[1]/form/table/tbody/tr[1]/td[2]/input',
              'password_field': '//*[@id="content"]/div[1]/div[1]/form/table/tbody/tr[2]/td[2]/input',
              'low_resolution_tickbox': '//*[@id="content"]/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/label/input',
              'login_button': '//*[@id="s1"]',
                'close_cookies': '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"]'}
    driver = webdriver.Chrome(r'C:\Users\nadav\Documents\Coding\misc\chromedriver.exe')
    driver.get('https://ts2.travian.com/')
    sleep(0.5)
    while True:
        try:
            driver.find_element_by_xpath(login_xpaths['close_cookies']).click()
            break
        except:
            sleep(0.5)
            pass
    driver.find_element_by_xpath(login_xpaths['username_field']).send_keys(email)
    driver.find_element_by_xpath(login_xpaths['password_field']).send_keys(password)
    if low_resolution:
        driver.find_element_by_xpath(login_xpaths['low_resolution_tickbox']).click()

    driver.find_element_by_xpath(login_xpaths['login_button']).click()

    return driver

def get_resources():
    pass
def get_production():
    pass
def get_fields():
    pass
def get_buildings():
    pass
def get_done_at():
    pass