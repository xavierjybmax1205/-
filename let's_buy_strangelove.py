import requests
import json
import selenium import webdriver
import time

def stockavailavity():
    request = requests.get('https://strangeloveskateboards.com/products.json')

    tee = json.loads((request.text))['products']


    for tee in products:
        name_of_the_shirt = tee['title']
        if name_of_the_shirt == 'StrangeLove Logo / Black / T-Shirt':
            
            producturl = 'https://strangeloveskateboards.com/products/' + tee['handle']
            return(producturl)
        else:
            return false

def purchaseproduct(url):
    driver = webdriver.Chrome(executable_path=r'\usr\local\bin\chromedriver')
    driver.get(str(url))
    driver.find_element_by_xpath('//div[@data-value="L"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//button[@id="AddToCart"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//button[@value="Check Out"]').click()
    time.sleep(4)
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("wnsdudgjf@gmail.com")
    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys("Junyoung")
    time.sleep(1)
    driver.find element by xpath('//input[@placeholder="Last name"]').send_keys("Bae")                                                             
    time.sleep(1)
    driver.find element by xpath('//input[@placeholder="Address"]').send_keys("Surisan-ro 40")
    time.sleep(2)
    driver.find element by xpath('//input[@placeholder="City"]').send_keys("Gunpo-Si")
    time.sleep(1)
    driver.find element by xpath('//input[@placeholder="Zip code"]').send_keys("15823")
    time.sleep(1)                                                                       
    driver.find element by xpath('//input[@placeholder="phone"').send_keys("01074771111")
                                                                           
myUrl=stockavailavity()
if myUrl != False:
    purchaseproduct(myUrl)
    break
else:
    print('no')
                                                                            
    
    
    
    
    

