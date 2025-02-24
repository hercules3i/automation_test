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
from findWorking import __findWorking,__findWorkingFrige
from SelectElement import __selectWorkOrder, __selectProductAtrribute, __enterMachines, __selectShift, __enterWorkers
from FillData import __fillDataToTable
options = Options()
options.add_experimental_option("detach", True)

browser = Chrome(options)
browser.maximize_window()
actionChains = ActionChains(browser)
link = "https://os.3i.com.vn/Admin/Account/Login?ReturnUrl=%2FAdmin"
username = "admin"
password = "winwin2021"

delay = 5
sleeping_time = 0.5


def __login():
    browser.find_element(By.ID, "UserName").send_keys(username)
    browser.find_element(By.ID, "Password").send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="true_inner"]/section/form/div[3]').click()


def __findToBom():
    # browser.get("https://vft.appsmartwork.com/Admin/Bom#/")
    #browser.get("https://vft.appsmartwork.com/Admin/Bom#/index?wfInstCode=2&wfInstName=Luồng%20sản%20xuất")
    browser.get("https://os.3i.com.vn/Admin/Bom#/index?wfInstCode=13910&wfInstName=Lu%E1%BB%93ng%20s%E1%BA%A3n%20xu%E1%BA%A5t%20t%E1%BB%A7%20%C4%91i%E1%BB%87n")
    # browser.get("https://os.3i.com.vn/Admin/Bom#/index?wfInstCode=17629&wfInstName=Lu%E1%BB%93ng%20s%E1%BA%A3n%20xu%E1%BA%A5t%20%E1%BB%91c%20v%C3%ADt")
    # WebDriverWait(browser, delay).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="contentMain"]/div/div/div/ul/li[1]'))
    # ).click()

# def __toggleInOrOut(in_or_out: str):
#     try:
#         in_or_out_element = browser.find_element(By.XPATH,
#                                                  '/html/body/div[4]/div/div[2]/div[4]/div[2]/div/form/div[2]/div/div[6]/div[2]/div/label[2]')

#         if in_or_out == "Xuất":
#             in_or_out_element.click()
#             time.sleep(2)
#     except:
#         raise Exception("__toggleInOrOut()")
def __enterWarehouse(warehouse: Warehouse, bom: Bom, in_out_value: str):
    actionChains.move_to_element(browser.find_element(By.CLASS_NAME, 'tab-content')).perform()
    time.sleep(sleeping_time)
    if in_out_value == "Đầu vào":
        browser.find_element(By.XPATH, '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[3]/div/div/ul/li[1]/div').click()
        browser.implicitly_wait(delay)
        if (bom.work_order) is not None: 
            __selectWorkOrder(bom.work_order,browser,delay)
        __selectShift(bom.shift, browser)
        __enterMachines(bom.machines, browser)
        __enterWorkers(bom.workers, browser)
        __fillDataToTable(warehouse.input.product_list, browser, delay,"Đầu vào")
        button_save = browser.find_element(By.XPATH,
                                           '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[2]')
        actionChains.move_to_element(button_save).perform()
        button_save.click()
        time.sleep(sleeping_time)
    elif in_out_value == "Đầu ra":
        browser.find_element(By.XPATH, '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[3]/div/div/ul/li[2]/div').click()
        # update_process = browser.find_element(By.XPATH,'//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[6]/div[3]/div/label[2]')
        # browser.execute_script("arguments[0].style.display = 'block';", update_process)
        # update_process.click()

        print("Đã vào đầu ra")
        # Cần chọn lại lệnh sản xuất cho đầu ra
        try:
            if bom.work_order is not None:
                browser.find_element(By.XPATH,
                             '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[1]/div/div/div[2]/div/div').click()
                __selectWorkOrder(bom.work_order,browser,delay)
                update_process = browser.find_element(By.XPATH,'//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[6]/div[3]/div/label[2]')
                update_process.click()
            __selectShift(bom.shift, browser)
            __enterMachines(bom.machines, browser)
            __enterWorkers(bom.workers, browser)
            __fillDataToTable(warehouse.output.product_list, browser, delay,"Đầu ra")
            button_save = browser.find_element(By.XPATH,
                                           '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[2]')
            actionChains.move_to_element(button_save).perform()
            button_save.click()
        except Exception as e:
            print(f"Lỗi khi gọi: {e}")

def handleInputOutput(bom: Bom):
    if bom.in_or_out == "Xuất":
        in_or_out_element = browser.find_element(By.XPATH,
                                                 '/html/body/div[4]/div/div[2]/div[4]/div[2]/div/form/div[2]/div/div[6]/div[2]/div/label[2]')
        in_or_out_element.click()

    if bom.in_or_out == "Nhập" or bom.in_or_out == "Nhập ":
        # __toggleInOrOut(bom.in_or_out)
        print("Xử lý Nhập")
        print("Xử lý Đầu vào cho Nhập")
        __enterWarehouse(bom.warehouse_in, bom, "Đầu vào")
        print("Xử lý Đầu ra cho Nhập")
        __enterWarehouse(bom.warehouse_in, bom, "Đầu ra")
    elif bom.in_or_out == "Xuất" or bom.in_or_out == "Xuất ":
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
                __findWorkingFrige(task.name_of_task,browser=browser, delay=delay)
                bom = task.list_boms[i_bom]
                handleInputOutput(bom)
                # button_save = browser.find_element(By.XPATH,
                #                                    '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[2]')
                # actionChains.move_to_element(button_save).perform()
                # button_save.click()

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