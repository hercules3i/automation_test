import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Task import TaskSimpleData
from selenium.common.exceptions import *
from Bom import Warehouse
from datetime import datetime

options = Options()
options.add_experimental_option("detach", True)

browser = Chrome(options)
browser.maximize_window()
actionChains = ActionChains(browser)
link = "https://vft.appsmartwork.com/Admin%2FAccount/Login"
username = "admin"
password = "winwin2021"

list_workings = ["Công đoạn kéo", "Công đoạn dập và ren",
                 "Nhiệt", "Xi mạ", "Đóng gói"]

delay = 10
sleeping_time = 0.25


def __login():
    browser.find_element(By.ID, "UserName").send_keys(username)
    browser.find_element(By.ID, "Password").send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="true_inner"]/section/form/div[3]').click()


def __findToBom():
    # browser.get("https://vft.appsmartwork.com/Admin/Bom#/")
    browser.get("https://vft.appsmartwork.com/Admin/Bom#/index?wfInstCode=2&wfInstName=Luồng%20sản%20xuất")
    # WebDriverWait(browser, delay).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="contentMain"]/div/div/div/ul/li[1]'))
    # ).click()


def __isWorkOrder(text, work_order) -> bool:
    list_text_words = text.split(' ')
    list_work_order_words = work_order.split(' ')

    if len(list_text_words) != len(list_work_order_words):
        return False

    i = 0
    while i < len(list_text_words):
        if list_text_words[i] != list_work_order_words[i]:
            return False
        i += 1

    return True


def __selectWorkOrder(work_order: str):
    try:
        if work_order is not None:
            work_order_element = browser.find_element(By.XPATH,
                                                      '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[1]/div/div/div[2]/div/div')
            time.sleep(sleeping_time)
            work_order_element.click()
            time.sleep(sleeping_time)
            input_work_order_element = work_order_element.find_element(By.TAG_NAME, 'input')
            time.sleep(sleeping_time)
            li_work_order = work_order_element.find_element(By.ID, 'ui-select-choices-0')

            count_id = 0
            is_load_more = False
            while True:
                id = f"ui-select-choices-row-0-{count_id}"

                try:
                    div_element = li_work_order.find_element(By.ID, id)
                    is_load_more = False
                    text = div_element.find_element(By.TAG_NAME, 'a').text
                    if __isWorkOrder(text, work_order):
                        input_work_order_element.send_keys(Keys.ENTER)
                        break
                    input_work_order_element.send_keys(Keys.ARROW_DOWN)
                    count_id += 1
                except Exception as e:
                    print(e.args)
                except:
                    if is_load_more:
                        break
                    else:
                        x_path = f'//*[@id="{id}"]/a/div/button'
                        li_work_order.find_element(By.XPATH, x_path).click()
                        is_load_more = True
                        count_id += 1

    except:
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


def __toggleInOrOut(in_or_out: str):
    try:
        in_or_out_element = browser.find_element(By.XPATH,
                                                 '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[2]/div/div[6]/div[2]/div/label[2]')

        if in_or_out == "Xuất":
            in_or_out_element.click()
    except:
        raise Exception("__toggleInOrOut()")


def __fillDataToTable(list_products: list):
    try:
        # check list product
        if len(list_products) == 0:
            return

        tbody = browser.find_element(By.XPATH, '//*[@id="1"]/div/table/tbody')
        trs = tbody.find_elements(By.TAG_NAME, 'tr')
        error_message = "__fillDataToTable()"
        if len(trs) == 0:
            error_message = "Attribute data is null"
            raise Exception

        for i in range(len(trs)):
            product = None
            i = i + 1
            # find product
            if product is None:
                time.sleep(sleeping_time)
                name_element = browser.find_element(By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[1]')
                time.sleep(sleeping_time)
                name = name_element.text
                for prod in list_products:
                    if name == prod.name:
                        product = prod
                        break

            if product is None:
                continue

            # enter quantity
            time.sleep(sleeping_time)
            quantity_element = WebDriverWait(browser, delay).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[2]'))
            )
            time.sleep(sleeping_time)
            input_quantity_element = quantity_element.find_element(By.TAG_NAME, 'input')
            input_quantity_element.clear()
            input_quantity_element.send_keys(product.quantity)

            # enter unit
            time.sleep(sleeping_time)
            unit_element = WebDriverWait(browser, delay).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[3]'))
            )
            time.sleep(sleeping_time)
            if len(unit_element.find_elements(By.TAG_NAME, 'span')) > 0:
                unit_element.find_element(By.TAG_NAME, 'span').click()
                time.sleep(sleeping_time)
                input_element = WebDriverWait(browser, delay).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="main-content-vatco"]/div[11]/input[1]'))
                )
                input_element.clear()
                time.sleep(sleeping_time)
                input_element.send_keys(product.unit)
                time.sleep(sleeping_time)
                input_element.send_keys(Keys.ARROW_DOWN)
                time.sleep(sleeping_time)
                input_element.send_keys(Keys.ENTER)
            else:
                if unit_element.text == "":
                    error_message = "Not found unit"
                    raise Exception

            # specification
            time.sleep(sleeping_time)
            specification_element = browser.find_element(By.XPATH, f'//*[@id="1"]/div/table/tbody/tr[{i}]/td[4]')
            time.sleep(sleeping_time)
            specification_element.find_element(By.TAG_NAME, 'input').send_keys(product.specification)

            # tail
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
    except Exception as e:
        raise Exception(error_message)


def __enterWarehouse(warehouse: Warehouse):
    actionChains.move_to_element(browser.find_element(By.CLASS_NAME, 'tab-content')).perform()
    time.sleep(sleeping_time)

    #input
    browser.find_element(By.XPATH, '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[3]/div/div/ul/li[1]/div').click()
    browser.implicitly_wait(delay)
    __fillDataToTable(warehouse.input.product_list)

    #output
    browser.find_element(By.XPATH, '//*[@id="contentMain"]/div[4]/div[2]/div/form/div[3]/div/div/ul/li[2]/div').click()
    time.sleep(sleeping_time)
    __fillDataToTable(warehouse.output.product_list)


def AutoTest(tasks: list):
    browser.get(link)
    __login()
    __findToBom()

    for task in tasks:
        # find working
        print(task.name_of_task)
        i_bom = 0
        count_case = 0
        count_error = 0
        while i_bom < len(task.list_boms):
            try:
                __findWorking(task.name_of_task)

                bom = task.list_boms[i_bom]
                __selectWorkOrder(bom.work_order)
                __selectShift(bom.shift)
                __enterMachines(bom.machines)
                __enterWorkers(bom.workers)
                __toggleInOrOut(bom.in_or_out)

                if bom.in_or_out == "Nhập":
                    __enterWarehouse(bom.warehouse_in)
                elif bom.in_or_out == "Xuất":
                    __enterWarehouse(bom.warehouse_out)

                # press save button
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
