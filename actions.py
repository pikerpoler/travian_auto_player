from selenium import webdriver
from time import sleep
from misc import Resources

# driver = webdriver.Chrome(r'C:\Users\nadav\Documents\Coding\misc\chromedriver.exe')


NISSIM_PATH_TO_CHROMEDRIVER = r'C:\Users\nadav\Documents\Coding\misc\chromedriver.exe'


def login(path_to_chromedriver, email, password, low_resolution=True):
    login_xpaths = {'username_field': '//*[@id="content"]/div[1]/div[1]/form/table/tbody/tr[1]/td[2]/input',
              'password_field': '//*[@id="content"]/div[1]/div[1]/form/table/tbody/tr[2]/td[2]/input',
              'low_resolution_tickbox': '//*[@id="content"]/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/label/input',
              'login_button': '//*[@id="s1"]',
                'close_cookies': '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"]'}
    driver = webdriver.Chrome(path_to_chromedriver)

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


CROP_FIELDS_XPATHS = ('//*[@id="resourceFieldContainer"]/div[2]/div',
                        '//*[@id="resourceFieldContainer"]/div[8]/div',
                        '//*[@id="resourceFieldContainer"]/div[9]/div',
                        '//*[@id="resourceFieldContainer"]/div[12]/div',
                        '//*[@id="resourceFieldContainer"]/div[13]/div',
                        '//*[@id="resourceFieldContainer"]/div[15]/div')

LUMBER_FIELDS_XPATHS = ('//*[@id="resourceFieldContainer"]/div[1]/div',
                        '//*[@id="resourceFieldContainer"]/div[3]/div',
                        '//*[@id="resourceFieldContainer"]/div[14]/div',
                        '//*[@id="resourceFieldContainer"]/div[17]/div')

CLAY_FIELDS_XPATHS = ('//*[@id="resourceFieldContainer"]/div[5]/div',
                        '//*[@id="resourceFieldContainer"]/div[6]/div',
                        '//*[@id="resourceFieldContainer"]/div[16]/div',
                        '//*[@id="resourceFieldContainer"]/div[18]/div')

IRON_FIELDS_XPATHS = ('//*[@id="resourceFieldContainer"]/div[4]/div',
                        '//*[@id="resourceFieldContainer"]/div[7]/div',
                        '//*[@id="resourceFieldContainer"]/div[10]/div',
                        '//*[@id="resourceFieldContainer"]/div[11]/div')

FIELDS_BY_RESOURCE = {'crop': CROP_FIELDS_XPATHS, 'lumber': LUMBER_FIELDS_XPATHS,
                      'clay': CLAY_FIELDS_XPATHS, 'iron': IRON_FIELDS_XPATHS}

PRODUCTION_XPATHS = {'lumber': '//*[@id="production"]/tbody/tr[1]/td[3]',
                     'clay': '//*[@id="production"]/tbody/tr[2]/td[3]',
                     'iron': '//*[@id="production"]/tbody/tr[3]/td[3]',
                     'crop': '//*[@id="production"]/tbody/tr[4]/td[3]'}  ##only in resource page!

RESOURCES_AMOUNTS_XPATHS = {'lumber': '//*[@id="l1"]',
                            'clay': '//*[@id="l2"]',
                            'iron': '//*[@id="l3"]',
                            'crop': '//*[@id="l4"]'}

CAPACITIES_XPATHS = {'warehouse': '//*[@id="stockBar"]/div[1]/div/div',
                     'granery': '//*[@id="stockBar"]/div[2]/div/div'}

FREECROP_XPATH = '//*[@id="stockBarFreeCrop"]'

def get_resources(driver):
    return driver.execute_script("return resources")


def clean_int(st):
    digits = '1234567890'
    clean_ls = ''.join([c for c in st if c in digits])
    return int(clean_ls)


def find_smallest_field(driver, resource):
    fields_xpaths = FIELDS_BY_RESOURCE[resource]

    xpath_and_lvl_ls = []
    for xpath in fields_xpaths:

        elem = driver.find_element_by_xpath(xpath)
        level = elem.text
        if level is '':
            level = 0
        else:
            level = int(level)

        xpath_and_lvl_ls += [(elem, level)]

    return min(xpath_and_lvl_ls, key=lambda x: x[1])


def upgrade_field(driver, resource):
    elem, level = find_smallest_field(driver, resource)

    elem.click()
    sleep(2)
    try:
        upgrade_button = driver.find_element_by_xpath('//*[@id="build"]/div[3]/div[4]/div[1]/button')
    except:
        sleep(.1)

    #     try:
    #         not_enough_resource_msg = driver.find_element_by_xpath('//*[@id="contract"]/div[2]/div')
    #         msg_text = not_enough_resource_msg.text
    #         if 'Enough resources on' in msg_text:
    #     except:
    #         pass

    if 'Construct with master builder' in upgrade_button.text:
        return
    else:
        upgrade_button.click()