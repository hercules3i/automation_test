import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# from Task import TaskSimpleData
from selenium.common.exceptions import *
from log import logger

# from Bom import Warehouse
from datetime import datetime
from task_test import __findToTasks
sleeping_time = 0.25


def __selectStaff(browser, list_staffs, jobcard_name):
    list_staffs = [staff for staff in list_staffs if staff.card_job.strip().lower() == jobcard_name.strip().lower()]
    list_staffs = list_staffs[0].list_staffs

    for i in range(len(list_staffs)):
        list_staffs[i] = list_staffs[i].strip().lower()
    print(str(list_staffs))
    # Tìm nút "display_departments_btn" trên giao diện web
    display_staffs_btn = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-modal/div/ion-content/div/div[3]/ion-item/ionic-selectable/div/button')
    if display_staffs_btn:
        display_staffs_btn.click()
    time.sleep(sleeping_time)
    # father_group_choices = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-modal[2]/ionic-selectable-modal/ion-content/ion-list/ion-item-group')
    # list_choices = father_group_choices.find_elements(By.TAG_NAME,'ion-label')
    # print(len(list_choices))
    # Tạm dừng trong một khoảng thời gian (nếu cần thiết)
    is_done = False
    for i in range(len(list_staffs)):
        search_input = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal[2]/ionic-selectable-modal/ion-header/ion-toolbar[2]/ion-searchbar/div/input')
        search_input.clear()
        time.sleep(sleeping_time)
        if list_staffs[i] == "tất cả":
            group_item_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal[2]/ionic-selectable-modal/ion-content/ion-list/ion-item-group')
            all_item_element = group_item_element.find_elements(By.TAG_NAME,'ion-item')
            for element in all_item_element:
                ActionChains(browser).move_to_element(element).perform()
                element.click()
                time.sleep(sleeping_time)
            ok_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal[2]/ionic-selectable-modal/ion-footer/ion-toolbar/ion-row/ion-col/ion-button')
            ok_element.click()
            time.sleep(0.5)
            break
        try:
            search_input.send_keys(list_staffs[i])
            time.sleep(3)
            father_group_choices = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-modal[2]/ionic-selectable-modal/ion-content/ion-list')
            item_selected = father_group_choices.find_element(By.TAG_NAME,'ion-item-group')
            item_selected.click()
            time.sleep(sleeping_time)
            ok_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal[2]/ionic-selectable-modal/ion-footer/ion-toolbar/ion-row/ion-col/ion-button')
            ok_element.click()
            time.sleep(0.5)
            break
        except Exception as e:
            cancel_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal[2]/ionic-selectable-modal/ion-header/ion-toolbar[1]/ion-buttons/ion-button')
            cancel_element.click()
            time.sleep(sleeping_time)
            logger.warning(f"{jobcard_name} - Khong co nhan vien ten: {list_staffs[i]}")
        
    # ok_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal[2]/ionic-selectable-modal/ion-footer/ion-toolbar/ion-row/ion-col/ion-button')
    # ok_element.click()
    # time.sleep(0.5)
    ok_done_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/div/ion-content/div/div[5]')
    ok_done_btn.click()
    # try:
    #         toast_container = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-toast').shadow_root
    #         message = toast_container.find_element(By.CLASS_NAME, 'toast-message').text
    #         message = message.split(" ")
    #         if "thành công" in message:
    #             logger.info(f"{jobcard_name} - {message}")
    #         else:
    #             logger.warning(f"{jobcard_name} - {message}")
    # except NoSuchElementException as e:
    #         logger.error(f"{jobcard_name} - Element not found: {e}")
    # except Exception as e:
    #         logger.error(f"{jobcard_name} - An error occurred: {e}", exc_info=True)
    logger.info(f"Thêm nhân sự cho 'jobcard_name' thành công")
    time.sleep(0.5)



def __selectDepartment(browser, list_staffs, jobcard_name):
    try:
        list_staffs = [staff for staff in list_staffs if staff.card_job.strip().lower() == jobcard_name.strip().lower()]
        list_departments = list_staffs[0].department_group
        # Cập nhật các phần tử của list_departments
        for i in range(len(list_departments)):
            list_departments[i] = list_departments[i].strip().lower()
            if list_departments[i] == None or list_departments[i] == "":
                list_departments[i] == "tất cả người dùng"
        print(str(list_departments))
        # Tìm nút "display_departments_btn" trên giao diện web
        display_departments_btn = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-modal/div/ion-content/div/div[2]/ion-item/ionic-selectable/div/button')
        display_departments_btn.click()
        time.sleep(0.5)
        while True:
            try:
                father_group_choices = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-modal[2]/ionic-selectable-modal/ion-content/ion-list')
            except:
                continue
            if father_group_choices:
                break
        list_choices = father_group_choices.find_elements(By.TAG_NAME,'ion-label')

        # Tạm dừng trong một khoảng thời gian (nếu cần thiết)
        time.sleep(sleeping_time)
        is_done = False
        for element in list_choices:
            print(((element.text).strip()).lower(),list_departments)
            if ((element.text).strip()).lower() in list_departments:
                element.click()
                is_done = True
                time.sleep(sleeping_time)
        if is_done == False:    
            all_users_label = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal[2]/ionic-selectable-modal/ion-content/ion-list/ion-item-group[1]/ion-item/ion-label')
            all_users_label.click()
            time.sleep(sleeping_time)
        ok_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal[2]/ionic-selectable-modal/ion-footer/ion-toolbar/ion-row/ion-col/ion-button')
        ok_element.click()
        time.sleep(sleeping_time)
    except:
        logger.warning(f"{jobcard_name} - Khong co phong ban nhom nao thoa man {str(list_departments)}")

def __selectBranch(browser, list_staffs, jobcard_name):
    try:
        # Lọc các staff có card_job bằng jobcard_name
        list_staffs = [staff for staff in list_staffs if (staff.card_job).strip().lower() == jobcard_name.strip().lower()]
        branch = list_staffs[0].branch_agency
        print(branch)
        # Tìm nút "display_branchs_btn" trên giao diện web
        display_branchs_btn = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-modal/div/ion-content/div/div[1]/ion-item/ionic-selectable/div/button')
        display_branchs_btn.click()
        # Tạm dừng trong một khoảng thời gian (nếu cần thiết)
        time.sleep(sleeping_time)
        branch = (branch.strip()).lower()
        branch_father_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal[2]/ionic-selectable-modal/ion-content/ion-list/ion-item-group')
        group_branch_label = branch_father_element.find_elements(By.TAG_NAME,'ion-label')
        for element in group_branch_label:
            print(((element.text).strip()).lower(), branch)
            if ((element.text).strip()).lower() == branch:
                element.click()
                break
    except:
        logger.warning(f"{jobcard_name} - Khong co nhanh nao thoa man {branch}")
        
        



def retry(func, browser, list_staffs, jobCard_name, max_retries=1):
    retries = 0
    while retries <= max_retries:
        try:
            func(browser, list_staffs, jobCard_name)
            break
        except Exception as e:
            retries += 1
            logger.error(f"{jobCard_name} - Error in {func.__name__}. Retry {retries}/{max_retries}: {e}")
            if retries > max_retries:
                logger.error(f"{jobCard_name} - Failed after {retries} attempts in {func.__name__}", exc_info=True)
                break
            time.sleep(1)  # Sleep before retrying

def __findToStaff(browser, list_staffs, jobCard_name, list_tasks):
    # try:
        time.sleep(1)
        apps_btn = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-footer/app-menu-footer/div/div[2]')
        apps_btn.click()
        time.sleep(sleeping_time)
        add_staff_app_btn = browser.find_element(By.XPATH, '//*[@id="main-content"]/app-create-card-job/ion-footer/app-menu-footer/div[1]/div/div[5]/div/div')
        add_staff_app_btn.click()
        time.sleep(sleeping_time)
        add_staff_btn_shadow = browser.find_element(By.XPATH, '//*[@id="main-content"]/app-create-card-job/ion-content/div/div[2]/div/div/app-working-schedule-assign/ion-content/div[1]/span/ion-icon').shadow_root
        add_staff_btn = add_staff_btn_shadow.find_element(By.CSS_SELECTOR, '[class="icon-inner"]')
        add_staff_btn.click()
        time.sleep(1)
        if len(list_staffs) != 0:
        # Retry these methods up to 1 more time in case of error
            retry(__selectBranch, browser, list_staffs, jobCard_name, max_retries=1)
            time.sleep(sleeping_time)
            retry(__selectDepartment, browser, list_staffs, jobCard_name, max_retries=1)
            time.sleep(sleeping_time)
            retry(__selectStaff, browser, list_staffs, jobCard_name, max_retries=1)
            time.sleep(sleeping_time)
        
        __findToTasks(browser, list_tasks, jobCard_name)
    # except Exception as e:
    #     logger.error(f"{jobCard_name} - An error occurred: {e}", exc_info=True)
