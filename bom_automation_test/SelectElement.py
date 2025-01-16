import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


sleeping_time = 0.5
def __isWorkOrder(text, work_order) -> bool:
    match = re.search(r'\[(.*?)\]', text)
    if match:
        extracted_value = match.group(1)  # Lấy nội dung trong ngoặc vuông

        if len(extracted_value) != len(work_order):
            return False
        extracted_words = extracted_value.split()
        work_order_words = work_order.split()
        if len(extracted_words) != len(work_order_words):
            return False
        for word1, word2 in zip(extracted_words, work_order_words):
            if word1 != word2:
                return False
        return True
    return False



def __selectWorkOrder(work_order: str,browser, delay:int):
    if not work_order:
        return
    try:
        if work_order is not None:
            work_order_element = WebDriverWait(browser, delay).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[1]/div/div/div[2]/div/div'))
            )
            work_order_element.click()
            time.sleep(sleeping_time)
            
            input_work_order_element = work_order_element.find_element(By.TAG_NAME, 'input')
            input_work_order_element.clear()
            input_work_order_element.send_keys(work_order)
            time.sleep(2)
            li_work_order = work_order_element.find_element(By.CLASS_NAME, 'ui-select-choices-group')

            count_id = 3
            is_load_more = False
            while True:
                xpath ='/html/body/div[4]/div/div[2]/div[4]/div[2]/div/form/div[2]/div/div[1]/div/div/div[2]/div/div/ul/li'
                try:
                    div_element = li_work_order.find_element(By.XPATH, xpath)
                    is_load_more = False
                    text = div_element.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div/form/div[2]/div/div[1]/div/div/div[2]/div/div/ul/li/div[{count_id}]/a").text
                    if __isWorkOrder(text, work_order):
                        input_work_order_element.send_keys(Keys.ARROW_DOWN)
                        input_work_order_element.send_keys(Keys.ENTER)  # Chọn work_order
                        break
                    input_work_order_element.send_keys(Keys.ARROW_DOWN)
                    count_id += 1

                except Exception as e:
                    print(f"Exception: {e.args}")
                    if is_load_more:
                        break
                    else:
                        x_path = f'//*[@id="{id}"]/a/div/button'
                        li_work_order.find_element(By.XPATH, x_path).click()
                        is_load_more = True
                        count_id += 1

    except Exception as e:
        print(f"Lỗi khi gọi __selectWorkOrder: {e}")
        raise Exception("__selectWorkOrder()")

def __isProductAtrribute(text: str, productAtrribute: str) -> bool:
    if len(text.strip()) != len(productAtrribute.strip()):
        return False
    list_text_words = text.split(' ')
    list_product_Atrribute_words = productAtrribute.split(' ')
    if len(list_text_words) != len(list_product_Atrribute_words):
        return False
    for i in range(len(list_product_Atrribute_words)):
        if list_product_Atrribute_words[i] != list_text_words[i]:
            return False
    return True

def __selectProductAtrribute(productAtrribute: str,browser, delay:int):
    try:
        if productAtrribute is not None:
            product_atrribute_element = WebDriverWait(browser, delay).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="modal-body"]/div/div/div/div/div/div/div[1]/form/div/div[1]/div/div'))
            )
            product_atrribute_element.click()
            time.sleep(sleeping_time)

            try:
                input_product_atrribute_element = WebDriverWait(product_atrribute_element, delay).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'input'))
                )
            except Exception as e:
                print("Không tìm thấy thẻ <input>:", e)
                return 
            time.sleep(sleeping_time)
            input_product_atrribute_element = WebDriverWait(product_atrribute_element, delay).until(
                EC.presence_of_element_located((By.TAG_NAME, 'input'))
            )
            input_product_atrribute_element.clear()
            input_product_atrribute_element.send_keys(productAtrribute)
            li_product_atrribute = product_atrribute_element.find_element(By.CLASS_NAME, 'ui-select-choices-group')
            is_load_more = False
            count_id = 3
            while True:
                try:
        # Tạo XPath động dựa trên count_id
                    xpath = f'/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div/div[1]/div/div/ul/li'
                    try:
                        div_element = li_product_atrribute.find_element(By.XPATH, xpath)
                        print(div_element)
                        is_load_more = False
                        text = div_element.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div/div[1]/div/div/ul/li/div[{count_id}]/a').text
                        print(text)
                        if __isProductAtrribute(text, productAtrribute):
                            input_product_atrribute_element.send_keys(Keys.ARROW_DOWN)
                            input_product_atrribute_element.send_keys(Keys.ENTER)
                            break
                        input_product_atrribute_element.send_keys(Keys.ARROW_DOWN)
                        count_id += 1
                    except Exception as e:
                        print(f"Không tìm thấy phần tử li[{count_id}]: {e}")
                        if is_load_more:
                            break
                        else:
                            # Thử tải thêm danh sách nếu có nút tải thêm
                            load_more_xpath = f'{xpath}/a/div/button'
                            try:
                                li_product_atrribute.find_element(By.XPATH, load_more_xpath).click()
                                is_load_more = True
                                count_id += 1
                            except Exception as click_e:
                                print(f"Lỗi khi tải thêm danh sách: {click_e}")
                                break

                except Exception as e:
                    print(f"Lỗi khi xử lý phần tử li[{count_id}]: {e}")
                    break
    except Exception as e:
        print(f"Lỗi khi gọi __selectProductAtrribute: {e}")
        raise Exception("__selectProductAtrribute()")
    
def __selectShift(shift: str, browser):
    try:
        shift_element = browser.find_element(By.XPATH,
                                             '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[2]/div/div/div[2]/div/div')
        shift_element.click()
        time.sleep(sleeping_time)
        li_shift = browser.find_element(By.XPATH, '//*[@id="ui-select-choices-1"]')
        time.sleep(sleeping_time)
        all_shifts = li_shift.find_elements(By.TAG_NAME, 'div')
        time.sleep(sleeping_time)

        for s in all_shifts:
            s_text = s.text
            if shift == s_text:
                s.click()
                break
    except:
        raise Exception("__selectShift()")


def __enterMachines(machines: list, browser):
    machines_element = browser.find_element(By.XPATH,
                                            '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[4]/div/div/div[2]/div/div[1]/input')
    for machine in machines:
        machines_element.send_keys(machine)
        machines_element.send_keys(Keys.ENTER)


    # if machines_element.text == "":
    #     raise ValueError("Machine: Not have machine")


def __enterWorkers(workers: list, browser):
    try:
        workers_element = browser.find_element(By.XPATH,
                                               '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[5]/div/div/div[2]/user-picker/div/div[1]/input')
        browser.execute_script("arguments[0].scrollIntoView();", workers_element)

        for worker in workers:
            workers_element.send_keys(worker)
            time.sleep(sleeping_time)
            workers_element.send_keys(Keys.ENTER)
    except:
        raise Exception("__enterWorkers()")

