crop_fields = ('//*[@id="resourceFieldContainer"]/div[2]/div', 
                '//*[@id="resourceFieldContainer"]/div[15]/div', 
                '//*[@id="resourceFieldContainer"]/div[8]/div', 
                '//*[@id="resourceFieldContainer"]/div[9]/div', 
                '//*[@id="resourceFieldContainer"]/div[13]/div', 
                '//*[@id="resourceFieldContainer"]/div[12]/div')

lumber_fields = ('//*[@id="resourceFieldContainer"]/div[1]/div',
                '//*[@id="resourceFieldContainer"]/div[3]/div',
                '//*[@id="resourceFieldContainer"]/div[17]/div',
                '//*[@id="resourceFieldContainer"]/div[14]/div')

clay_fields = ('//*[@id="resourceFieldContainer"]/div[5]/div',
                '//*[@id="resourceFieldContainer"]/div[6]/div',
                '//*[@id="resourceFieldContainer"]/div[18]/div',
                '//*[@id="resourceFieldContainer"]/div[16]/div')

iron_fields = ('//*[@id="resourceFieldContainer"]/div[4]/div',
                '//*[@id="resourceFieldContainer"]/div[7]/div',
                '//*[@id="resourceFieldContainer"]/div[11]/div',
                '//*[@id="resourceFieldContainer"]/div[10]/div')

fields_xpaths = {'crop': crop_fields, 'lumber': lumber_fields, 
                 'clay': clay_fields, 'iron': iron_fields}	

production_xpaths = {'lumber': '//*[@id="production"]/tbody/tr[1]/td[3]', 
                     'clay': '//*[@id="production"]/tbody/tr[2]/td[3]', 
                     'iron': '//*[@id="production"]/tbody/tr[3]/td[3]', 
                     'crop': '//*[@id="production"]/tbody/tr[4]/td[3]'} ##only in resource page!

resources_amounts_xpaths = {'lumber': '//*[@id="l1"]', 
                            'clay': '//*[@id="l2"]', 
                            'iron': '//*[@id="l3"]', 
                            'crop': '//*[@id="l4"]'}

capacities_xpaths = {'warehouse': '//*[@id="stockBar"]/div[1]/div/div', 
                     'granery': '//*[@id="stockBar"]/div[2]/div/div'}


def get_resources():
    xpaths = [resources_amounts_xpaths[res] for res in ['lumber', 'clay', 'iron', 'crop']]
    amounts = [int(driver.find_element_by_xpath(xpath).text) for xpath in xpaths]    
    
    return Resources(*amounts)
        

def get_capacity():
    warehouse_capacity = int(driver.find_element_by_xpath(capacities_xpaths['warehouse']).text[1:-1])
    granery_capacity = int(driver.find_element_by_xpath(capacities_xpaths['granery']).text[1:-1])
    
    return Resources(warehouse_capacity, warehouse_capacity, warehouse_capacity, granery_capacity)

def get_production():  # TODO: check you are in resource page, otherwisw go there
    xpaths = [production_xpaths[res] for res in ['lumber', 'clay', 'iron', 'crop']]
    prod = [int(driver.find_element_by_xpath(xpath).text[1:-1]) for xpath in xpaths]
    
    return Resources(*prod)
