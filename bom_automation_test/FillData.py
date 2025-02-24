import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from SelectElement import __selectWorkOrder, __selectProductAtrribute

sleeping_time = 0.5

def __fillExtendedDataToTable(row_index: int, browser, delay: int, product):
    attribute_element = WebDriverWait(browser, delay).until(
            EC.element_to_be_clickable((By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{row_index}]/td[last()]'))
        )
    browser.execute_script("arguments[0].scrollIntoView(true);", attribute_element)
    time.sleep(sleeping_time)
    attribute_element.click()
    product_attributes = {
        'Tiêu hao có thể thu hồi': product.recoverable_cost,
        'SCRAP': product.scrap,
        'LOSS_RATIO': product.lost_rati,
        'Tiêu hao': product.cost,
        'Loại thép': product.steel_type
    }
    for attr_name, attr_value in product_attributes.items():
        print(attr_name)
        __selectProductAtrribute(attr_name,browser,delay)
        value_input = browser.find_element(By.XPATH,'//*[@id="modal-body"]/div/div/div/div/div/div/div[1]/form/div/div[2]/div/input')
        value_input.clear()
        value_input.send_keys(str(attr_value)) 
        new_button = browser.find_element(By.XPATH,'//*[@id="modal-body"]/div/div/div/div/div/div/div[1]/form/div/div[3]/div[1]/div/a/i')
        new_button.click()
    save_button = browser.find_element(
        By.XPATH,
        '//*[@id="main-content-vatco"]/div[1]/div/div/div[1]/div'
    )
    save_button.get_attribute('outerHTML')
    save_button.click()

def __fillDataToTable(product_list: list, browser, delay:int, in_out_value: str):
    try:
        if len(product_list) == 0:
            return
        print(len(product_list))
        tbody = browser.find_element(By.XPATH, '//*[@id="1"]/div/table/tbody')
        trs = tbody.find_elements(By.TAG_NAME, 'tr')

        if len(trs) == 0:
            raise Exception("Attribute data is null")
        for i in range(len(trs)):
            i = i + 1 
            # Enter quantity = 0
            time.sleep(sleeping_time)
            quantity_element = WebDriverWait(browser, delay).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[2]'))
            )
            input_quantity_element = quantity_element.find_element(By.TAG_NAME, 'input')
            input_quantity_element.clear()
            input_quantity_element.send_keys(0)
        for i in range(len(trs)):
            product = None
            i = i + 1  # Tăng chỉ số dòng lên 1

            # Find product in the product list
            if product is None:
                time.sleep(sleeping_time)
                name_element = browser.find_element(By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[1]')
                time.sleep(sleeping_time)
                name = name_element.text
                print(f"name:{name}")
                for prod in product_list:
                    print(prod.name)
                    if name == prod.name:
                        product = prod
                        break

            if product is None:
                continue

            # Enter quantity
            time.sleep(sleeping_time)
            quantity_element = WebDriverWait(browser, delay).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[2]'))
            )
            time.sleep(sleeping_time)
            input_quantity_element = quantity_element.find_element(By.TAG_NAME, 'input')
            input_quantity_element.clear()
            input_quantity_element.send_keys(product.quantity)
            
            if in_out_value == "Đầu vào":
                # Enter unit
                time.sleep(sleeping_time)
                unit_element = WebDriverWait(browser, delay).until(
                    EC.presence_of_element_located((By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div/form/div[3]/div/div/div/div/div/table/tbody/tr[{i}]/td[3]'))                  
                )
                time.sleep(1)
                if len(unit_element.find_elements(By.TAG_NAME, 'span')) > 0:
                    unit_element.find_element(By.TAG_NAME, 'span').click()
                    time.sleep(1)
                    input_element = WebDriverWait(browser, delay).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content-vatco"]/div[11]/input[1]'))
                    )
                    input_element.clear()
                    input_element.send_keys(product.unit)
                    input_element.send_keys(Keys.ARROW_DOWN)
                    input_element.send_keys(Keys.ENTER)
                else:
                    if unit_element.text == "":
                        raise Exception("Not found unit")
            else:
                pass
            if product.specification is not None:
                time.sleep(sleeping_time)
                specification_element = browser.find_element(By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[4]')
                time.sleep(sleeping_time)
                input_specification_element = specification_element.find_element(By.TAG_NAME, 'input')
                input_specification_element.clear()
                input_specification_element.send_keys(product.specification)
            if product.tail is not None:
                time.sleep(sleeping_time)
                tail_element = browser.find_element(By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[5]')
                time.sleep(sleeping_time)
                tail_element.find_element(By.TAG_NAME, 'input').send_keys(product.tail)
            if product.not_good is not None:
                time.sleep(sleeping_time)
                not_good_element = browser.find_element(By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[6]')
                time.sleep(sleeping_time)
                not_good_element.find_element(By.TAG_NAME, 'input').send_keys(product.not_good)
            if product.recoverable_cost is not None:
                print(product.recoverable_cost)
                __fillExtendedDataToTable(i,browser,delay,product)
            else:
                pass
    except Exception as e:
        print(f"Error in __fillDataToTable: {e}")
        raise
