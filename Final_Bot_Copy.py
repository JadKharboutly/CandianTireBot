from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.canadiantire.ca/en/pdp/cap-barbell-dumbbell-weights-set-40-lb-0840760p.html")
time.sleep(5)


def check_out():
    Checkout = driver.find_element_by_css_selector("body > div.success-popup.success-popup_sidebar > div > div > div.popup-component__container__body > div > div.popup-component__container__body.nano-content > div.success-popup__product > div.success-popup__buttons-wrapper > a.success-popup__button.success-popup__cart-button")
    Checkout.click()


    time.sleep(5)

    check = driver.find_element_by_css_selector("body > div.parsys.content-paragraph > div.parbase.section.shopping-cart-main > div > div > div.shopping-cart-main__sidebar > div > div > div > div:nth-child(2) > div.checkout-order-summary__panel__body > div.checkout-order-summary__continue-btn-wrapper.checkout-order-summary__continue-btn-wrapper--desktop > button.checkout-order-summary__continue-btn")

    check.click()

    time.sleep(5)
    
    phone = driver.find_element_by_id("opc-contact-details-form__text-input--telephone")
    email = driver.find_element_by_id("opc-contact-details-form__text-input--email")
    name = driver.find_element_by_id("opc-billing-form__text-input--first-name")
    nameLast = driver.find_element_by_id("opc-billing-form__text-input--last-name")
    address = driver.find_element_by_id("opc-billing-form__text-input--street-address")
    city = driver.find_element_by_id("opc-billing-form__text-input--city")
    postalCode = driver.find_element_by_id("opc-billing-form__text-input--postal-code")
    province = driver.find_element_by_css_selector("#opc-billing-form__text-input--province > option:nth-child(10)")
    country = driver.find_element_by_css_selector("#opc-billing-form__text-input--country > option:nth-child(41)")
    province.click()

    i=0
    email.send_keys(Keys.TAB)
    while i < 8:
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        i+= 1
    
    actions = ActionChains(driver)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    ''''' Date '''''
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    '''' CVV '''
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.send_keys(Keys.NUMPAD9)
    actions.perform()

    
    email.send_keys("example@gmail.com")
    phone.send_keys("999999999")
    name.send_keys("name")
    nameLast.send_keys("lastname")
    address.send_keys("1234 example st")
    city.send_keys("Toronto")
    postalCode.send_keys("L5H")
    time.sleep(5)

    
stock_status = driver.find_element_by_class_name("stock-status__title").text
store_options = driver.find_element_by_class_name("out-of-stock__header").text



while True:
    
    stock_status = driver.find_element_by_class_name("stock-status__title").text
    store_options = driver.find_element_by_class_name("out-of-stock__header").text
    
    if store_options == "Store options:" or stock_status == "IN-STORE"  :
        break
    else:
        driver.refresh()
        print("WAITING FOR RESTOCK...")
        time.sleep(60)
        

try:
    stock = driver.find_elements_by_class_name("instock-quantity")
    store_numbers = int(len(stock))
        
    unsorted_stock_list = []
    stock_list = []
    for i in range(store_numbers):
        unsorted_stock_list.append(int(stock[i].text.split(" ")[0]))
        stock_list.append(int(stock[i].text.split(" ")[0]))
    stock_list.sort(reverse = True)


    if (int(len(unsorted_stock_list)))<5:
                

        stock = driver.find_elements_by_class_name("instock-quantity")
        store_numbers = int(len(stock))
        
        unsorted_stock_list = []
        stock_list = []
        for i in range(store_numbers):
            unsorted_stock_list.append(int(stock[i].text.split(" ")[0]))
            stock_list.append(int(stock[i].text.split(" ")[0]))
        stock_list.sort(reverse = True)

        index = unsorted_stock_list.index(stock_list[0])
        print(stock_list)
        

        driver.implicitly_wait(5)
                            
        '''   '''
        
        store = driver.find_elements_by_class_name("out-of-stock__list__item__store-name")
        store_list = []
                
        for x in range(store_numbers):
            store_list.append(store[x].text)

        store[index].click()

        '''  '''
        add_to_cart_button = driver.find_element_by_css_selector("body > div.pdp-product-image-and-buy-box.base-pdp-buy-box > div > div.pdp-buy-box > div.product-buy-box.section > div > section.pdp-buy-box__secondary-section > div.delivery-options > div > div.delivery-option__wrapper > section > div.delivery-option__cta.in-store-pick-up-option > div > button")
        add_to_cart_button.click()

        driver.implicitly_wait(3)
        check_out()
        

except:

    try: 
        view_more_stores = driver.find_element_by_css_selector("#out-of-stock__list > button")
        view_more_stores_text = driver.find_element_by_css_selector("#out-of-stock__list > button").text

            
        if view_more_stores.text == view_more_stores_text:
            view_more_stores.click()
            driver.implicitly_wait(5)
            stock = driver.find_elements_by_class_name("instock-quantity")
            store_numbers = int(len(stock))
        
            unsorted_stock_list = []
            stock_list = []
            for i in range(store_numbers):
                unsorted_stock_list.append(int(stock[i].text.split(" ")[0]))
                stock_list.append(int(stock[i].text.split(" ")[0]))

            stock_list.sort(reverse = True)
        
            index = unsorted_stock_list.index(stock_list[0])
            print(stock_list)
        

            driver.implicitly_wait(5)
                            
            '''   '''
        
            store = driver.find_elements_by_class_name("out-of-stock__list__item__store-name")
            store_list = []
        
            for x in range(store_numbers):
                store_list.append(store[x].text)

            store[index].click()

            '''  '''
            add_to_cart_button = driver.find_element_by_css_selector("body > div.pdp-product-image-and-buy-box.base-pdp-buy-box > div > div.pdp-buy-box > div.product-buy-box.section > div > section.pdp-buy-box__secondary-section > div.delivery-options > div > div.delivery-option__wrapper > section > div.delivery-option__cta.in-store-pick-up-option > div > button")
            add_to_cart_button.click()
            driver.implicitly_wait(3)
            check_out()
                    

    except:

        stock_status = driver.find_element_by_class_name("stock-status__title").text

        if stock_status == "IN-STORE":
            add_to_cart_button = driver.find_element_by_css_selector("body > div.pdp-product-image-and-buy-box.base-pdp-buy-box > div > div.pdp-buy-box > div.product-buy-box.section > div > section.pdp-buy-box__secondary-section > div.delivery-options > div > div.delivery-option__wrapper > section > div.delivery-option__cta.in-store-pick-up-option > div > button")
            add_to_cart_button.click()
            driver.implicitly_wait(3)
            check_out()
                    
        
        
    
    





    
    
  
    

        
    
    

        
    

    



