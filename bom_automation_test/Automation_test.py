import time
import re
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Task import TaskSimpleData
from selenium.common.exceptions import *
from Bom import Warehouse, Bom
from datetime import datetime

options = Options()
options.add_experimental_option("detach", True)

browser = Chrome(options)
browser.maximize_window()
actionChains = ActionChains(browser)
link = "https://os.3i.com.vn/Admin/Account/Login?ReturnUrl=%2FAdmin"
username = "admin"
password = "winwin2021"

list_workings = ["Công đoạn kéo", "Công đoạn dập và ren",
                 "Nhiệt", "Xi mạ", "Đóng gói"]

delay = 10
sleeping_time = 1


def __login():
    browser.find_element(By.ID, "UserName").send_keys(username)
    browser.find_element(By.ID, "Password").send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="true_inner"]/section/form/div[3]').click()


def __findToBom():
    # browser.get("https://vft.appsmartwork.com/Admin/Bom#/")
    #browser.get("https://vft.appsmartwork.com/Admin/Bom#/index?wfInstCode=2&wfInstName=Luồng%20sản%20xuất")
    browser.get("https://os.3i.com.vn/Admin/Bom#/index?wfInstCode=17629&wfInstName=Lu%E1%BB%93ng%20s%E1%BA%A3n%20xu%E1%BA%A5t%20%E1%BB%91c%20v%C3%ADt")
    # WebDriverWait(browser, delay).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="contentMain"]/div/div/div/ul/li[1]'))
    # ).click()


def __isWorkOrder(text, work_order) -> bool:
    match = re.search(r'\[(.*?)\]', text)
    if match:
        extracted_value = match.group(1)  # Lấy nội dung trong ngoặc vuông
        # Kiểm tra độ dài
        if len(extracted_value) != len(work_order):
            return False
        # Kiểm tra từng từ
        extracted_words = extracted_value.split()
        work_order_words = work_order.split()
        if len(extracted_words) != len(work_order_words):
            return False
        for word1, word2 in zip(extracted_words, work_order_words):
            if word1 != word2:
                return False
        return True
    return False


def __selectWorkOrder(work_order: str):
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
            time.sleep(sleeping_time)
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

def __findWorking(nameTask: str):
    browser.implicitly_wait(delay)
    match nameTask:
        case "Công đoạn kéo":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[1]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Công đoạn dập và ren":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[2]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Nhiệt":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[3]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Xi mạ":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[4]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Đóng gói":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[5]/div/div/label/div/div/div/div/div/a/div/span').click()


def __selectShift(shift: str):
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


def __enterMachines(machines: list):
    machines_element = browser.find_element(By.XPATH,
                                            '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[4]/div/div/div[2]/div/div[1]/input')
    for machine in machines:
        machines_element.send_keys(machine)
        machines_element.send_keys(Keys.ENTER)


    # if machines_element.text == "":
    #     raise ValueError("Machine: Not have machine")


def __enterWorkers(workers: list):
    try:
        workers_element = browser.find_element(By.XPATH,
                                               '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[5]/div/div/div[2]/user-picker/div/div[1]/input')
        browser.execute_script("arguments[0].scrollIntoView();", workers_element)

        for worker in workers:
            workers_element.send_keys(worker)
            time.sleep(0.5)
            workers_element.send_keys(Keys.ENTER)
    except:
        raise Exception("__enterWorkers()")


# def __toggleInOrOut(in_or_out: str):
#     try:
#         in_or_out_element = browser.find_element(By.XPATH,
#                                                  '/html/body/div[4]/div/div[2]/div[4]/div[2]/div/form/div[2]/div/div[6]/div[2]/div/label[2]')

#         if in_or_out == "Xuất":
#             in_or_out_element.click()
#             time.sleep(2)
#     except:
#         raise Exception("__toggleInOrOut()")

# Đối với dữ liệu có thuộc tính mở rộng

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

def __selectProductAtrribute(productAtrribute: str):
    try:
        if productAtrribute is not None:
            product_atrribute_element = WebDriverWait(browser, delay).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="modal-body"]/div/div/div/div/div/div/div[1]/form/div/div[1]/div/div'))
            )
            time.sleep(1)
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

def __fillExtendedDataToTable(row_index: int, product):
    try:
        attribute_element = browser.find_element(By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{row_index}]/td[last()]')
        attribute_element.click()
    except (NoSuchElementException, ElementClickInterceptedException):
        print(f"Unable to click element at row {row_index}.")
        raise
    product_attributes = {
        'Tiêu hao có thể thu hồi': product.recoverable_cost,
        'SCRAP': product.scrap,
        'LOSS_RATIO': product.lost_rati,
        'Tiêu hao': product.cost,
        'Loại thép': product.steel_type
    }
    for attr_name, attr_value in product_attributes.items():
        print(attr_name)
        __selectProductAtrribute(attr_name)
        value_input = browser.find_element(By.XPATH,'//*[@id="modal-body"]/div/div/div/div/div/div/div[1]/form/div/div[2]/div/input')
        value_input.clear()
        value_input.send_keys(str(attr_value)) 
        new_button = browser.find_element(By.XPATH,'//*[@id="modal-body"]/div/div/div/div/div/div/div[1]/form/div/div[3]/div[1]/div/a/i')
        new_button.click()
    save_button = browser.find_element(
        By.XPATH,
        '//*[@id="main-content-vatco"]/div[1]/div/div/div[3]/div/div[2]'
    )
    save_button.click()

def __fillDataToTable(product_list: list, in_out_value: str):
    try:
        if len(product_list) == 0:
            return

        tbody = browser.find_element(By.XPATH, '//*[@id="1"]/div/table/tbody')
        trs = tbody.find_elements(By.TAG_NAME, 'tr')

        if len(trs) == 0:
            raise Exception("Attribute data is null")
        for i in range(len(trs)):
            i = i + 1  # Tăng chỉ số dòng lên 1

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
                for prod in product_list:
                    if name == prod.name:
                        product = prod
                        break

            if product is None:
                continue

            # Enter quantity
            time.sleep(sleeping_time)
            quantity_element = WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[2]'))
            )
            time.sleep(sleeping_time)
            input_quantity_element = quantity_element.find_element(By.TAG_NAME, 'input')
            input_quantity_element.clear()
            input_quantity_element.send_keys(product.quantity)
            
            if in_out_value == "Đầu vào":
                # Enter unit
                time.sleep(sleeping_time)
                unit_element = WebDriverWait(browser, 2).until(
                    EC.presence_of_element_located((By.XPATH, f'  /html/body/div[4]/div/div[2]/div[4]/div[2]/div/form/div[3]/div/div/div/div/div/table/tbody/tr[{i}]/td[3]'))                  
                )
                time.sleep(sleeping_time)
                if len(unit_element.find_elements(By.TAG_NAME, 'span')) > 0:
                    unit_element.find_element(By.TAG_NAME, 'span').click()
                    time.sleep(sleeping_time)
                    input_element = WebDriverWait(browser, 2).until(
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

            # Enter specification
            time.sleep(sleeping_time)
            specification_element = browser.find_element(By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[4]')
            time.sleep(sleeping_time)

            input_specification_element=specification_element.find_element(By.TAG_NAME, 'input')
            input_specification_element.clear()
            input_specification_element.send_keys(product.specification)

            # Enter tail
            if product.tail is not None:
                time.sleep(sleeping_time)
                tail_element = browser.find_element(By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[5]')
                time.sleep(sleeping_time)
                tail_element.find_element(By.TAG_NAME, 'input').send_keys(product.tail)

            # Enter not_good
            if product.not_good is not None:
                time.sleep(sleeping_time)
                not_good_element = browser.find_element(By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[6]')
                time.sleep(sleeping_time)
                not_good_element.find_element(By.TAG_NAME, 'input').send_keys(product.not_good)
            __fillExtendedDataToTable(i,product)
    except Exception as e:
        print(f"Error in __fillDataToTable: {e}")
        raise

def __enterWarehouse(warehouse: Warehouse, bom: Bom, in_out_value: str):
    actionChains.move_to_element(browser.find_element(By.CLASS_NAME, 'tab-content')).perform()
    time.sleep(sleeping_time)

    # Xử lý Đầu vào
    if in_out_value == "Đầu vào":
        browser.find_element(By.XPATH, '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[3]/div/div/ul/li[1]/div').click()
        browser.implicitly_wait(delay)
        if (bom.work_order) is not None: 
            __selectWorkOrder(bom.work_order)
        
        __selectShift(bom.shift)
        __enterMachines(bom.machines)
        __enterWorkers(bom.workers)
        __fillDataToTable(warehouse.input.product_list,"Đầu vào")
        time.sleep(5)
        button_save = browser.find_element(By.XPATH,
                                           '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[2]')
        actionChains.move_to_element(button_save).perform()
        button_save.click()
        time.sleep(5)

    # Xử lý Đầu ra
    elif in_out_value == "Đầu ra":
        time.sleep(2)
        browser.find_element(By.XPATH, '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[3]/div/div/ul/li[2]/div').click()
        # update_process = browser.find_element(By.XPATH,'//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[6]/div[3]/div/label[2]')
        # browser.execute_script("arguments[0].style.display = 'block';", update_process)
        # update_process.click()
        time.sleep(2)
        print("Đã vào đầu ra")
        # Cần chọn lại lệnh sản xuất cho đầu ra
        try:
            if bom.work_order is not None:
                browser.find_element(By.XPATH,
                             '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[1]/div/div/div[2]/div/div').click()
                __selectWorkOrder(bom.work_order)
                update_process = browser.find_element(By.XPATH,'//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[6]/div[3]/div/label[2]')
                update_process.click()
            __selectShift(bom.shift)
            __enterMachines(bom.machines)
            __enterWorkers(bom.workers)
            __fillDataToTable(warehouse.output.product_list,"Đầu ra")
        except Exception as e:
            print(f"Lỗi khi gọi: {e}")

def handleInputOutput(bom: Bom):
    if bom.in_or_out == "Xuất":
        in_or_out_element = browser.find_element(By.XPATH,
                                                 '/html/body/div[4]/div/div[2]/div[4]/div[2]/div/form/div[2]/div/div[6]/div[2]/div/label[2]')
        in_or_out_element.click()

    if bom.in_or_out == "Nhập":
        # __toggleInOrOut(bom.in_or_out)
        print("Xử lý Nhập")
        print("Xử lý Đầu vào cho Nhập")
        __enterWarehouse(bom.warehouse_in, bom, "Đầu vào")
        print("Xử lý Đầu ra cho Nhập")
        __enterWarehouse(bom.warehouse_in, bom, "Đầu ra")
    elif bom.in_or_out == "Xuất":
        # __toggleInOrOut(bom.in_or_out)
        print("Xử lý Xuất")
        print("Xử lý Đầu vào cho Xuất")
        __enterWarehouse(bom.warehouse_out, bom, "Đầu vào")   
        print("Xử lý Đầu ra cho Xuất")
        __enterWarehouse(bom.warehouse_out, bom, "Đầu ra")


def AutoTest(tasks: list):
    browser.get(link)
    __login()
    __findToBom()

    for task in tasks:
        print(task.name_of_task)
        i_bom = 0
        count_case = 0
        count_error = 0
        while i_bom < len(task.list_boms):
            try:
                __findWorking(task.name_of_task)
                bom = task.list_boms[i_bom]
                handleInputOutput(bom)
                button_save = browser.find_element(By.XPATH,
                                                   '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[2]')
                actionChains.move_to_element(button_save).perform()
                button_save.click()

                toast_container = browser.find_element(By.ID, 'toast-container')
                message = toast_container.find_element(By.CLASS_NAME, 'toast-message').text
                if message == "Thêm thành công":
                    print(f"Case: {count_case + 1} - {bom.work_order} - {bom.shift} - Success")
                    with open("successful_log", "a", encoding="utf-8") as f:
                        f.write(
                            f"{datetime.now()} - {task.name_of_task} - Case: {count_case + 1} - {bom.work_order} - {bom.shift}\n")
                else:
                    raise ValueError(message)

                count_case += 1
                i_bom += 1
            except ValueError as e:
                error_txt = repr(e)
                error_txt = f"Failed: {error_txt.split("'")[1]}"
                print(f"Case: {count_case + 1} - {bom.work_order} - {bom.shift} - {error_txt}")
                with open("failed_log", "a", encoding="utf-8") as f:
                    f.write(
                        f"{datetime.now()} - {task.name_of_task} - Case: {count_case + 1} - {bom.work_order} - {bom.shift} - {error_txt}\n")
                count_case += 1
                i_bom += 1
            except Exception as e:
                error_txt = repr(e)
                if error_txt == "Exception('Not found unit')" or error_txt == "Exception('Attribute data is null')":
                    error_txt = f"Failed: {error_txt.split("'")[1]}"
                    print(f"Case: {count_case + 1} - {bom.work_order} - {bom.shift} - {error_txt}\n")
                    with open("failed_log", "a", encoding="utf-8") as f:
                        f.write(
                            f"{datetime.now()} - {task.name_of_task} - Case: {count_case + 1} - {bom.work_order} - {bom.shift} - {error_txt}\n")
                    count_case += 1
                    i_bom += 1
                else:
                    if count_error == 2:
                        print(f"Case: {count_case + 1} - {task.name_of_task} - {bom.work_order} - {bom.shift} - {error_txt}")

                        with open("error_log", "a", encoding="utf-8") as f:
                            f.write(
                                f"{datetime.now()} - {task.name_of_task} - Case: {count_case + 1} - {bom.work_order} - {bom.shift} - {error_txt}\n")

                        count_error = 0
                        i_bom += 1
                        count_case += 1
                    count_error += 1
            finally:
                browser.refresh()
                time.sleep(1)