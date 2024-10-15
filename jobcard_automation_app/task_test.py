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
# from Bom import Warehouse
from datetime import datetime
from log import logger

sleeping_time = 0.25

def __selectUnit(browser, task):
    display_list_units_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-check-list-add-user/ion-content/div[2]/div[3]/ion-item/ionic-selectable/div/button')
    display_list_units_btn.click()
    time.sleep(sleeping_time)
    search_input = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-header/ion-toolbar[2]/ion-searchbar/div/input')
    search_input.clear()
    search_input.send_keys(task.unit.strip().lower())
    time.sleep(3)
    father_group_choices = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list')
    item_selected = father_group_choices.find_element(By.TAG_NAME,'ion-item-group')
    item_selected.click()
    time.sleep(sleeping_time)

def __selectDuration(browser, task):
    insert_duration_input = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-check-list-add-user/ion-content/div[2]/div[2]/input')
    insert_duration_input.clear()
    insert_duration_input.send_keys(task.duration)
    time.sleep(sleeping_time)

def __select_staff(browser,task):
    select_user_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-check-list-add-user/ion-content/div[2]/div[1]/ion-item/ionic-selectable/div/button')
    select_user_btn.click()
    time.sleep(sleeping_time)
    # for i in range(len(list_staffs)):
    search_input = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-header/ion-toolbar[2]/ion-searchbar/div/input')
    search_input.clear()
    search_input.send_keys(task.staff.strip().lower())
    time.sleep(3)
    father_group_choices = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list')
    item_selected = father_group_choices.find_element(By.TAG_NAME,'ion-item-group')
    item_selected.click()
    time.sleep(sleeping_time)
        
def __findToAddStaff(browser,task):
    add_staff_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-content/div/div[2]/div/div/ion-item/ion-row/ion-col[4]/i')
    add_staff_btn.click()
    time.sleep(sleeping_time)
    __select_staff(browser,task)
    __selectDuration(browser, task)
    __selectUnit(browser,task)
    save_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-check-list-add-user/ion-content/div[2]/div[4]/a')
    save_btn.click()
    try:
            toast_container = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-toast').shadow_root
            message = toast_container.find_element(By.CLASS_NAME, 'toast-message').text
            print(message)
            if "thành công" in message:
                logger.info(message)
            else:
                logger.warning(message)
    except NoSuchElementException as e:
            logger.error(f"Element not found: {e}")
    except Exception as e:
            logger.error(f"An error occurred: {e}", exc_info=True)

    time.sleep(1)   
    
    

def __insert_task_name(browser, task):
    
    div_edit_content = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/div/ion-content/quill-editor/div/div[1]')
    div_edit_content.clear()
    if task.name != None:
        div_edit_content.send_keys(task.name)
    else:
        div_edit_content.send_keys()
        
    time.sleep(sleeping_time)
    weight_input_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/div/ion-header/ion-toolbar/div/input')
    weight_input_element.clear()
    weight_input_element.send_keys(task.weight)
    time.sleep(sleeping_time)
    post_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/div/ion-header/ion-toolbar/ion-buttons[2]/ion-button')
    post_btn.click()
    time.sleep(0.5)
    __findToAddStaff(browser, task)
    
        

def __findToTasks(browser, list_tasks,jobCard_name):

    add_task_app_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-footer/app-menu-footer/div[1]/div/div[2]/div/div')
    add_task_app_btn.click()
    time.sleep(sleeping_time)

    tasks = []
    for task in list_tasks:
        if jobCard_name.strip().lower() == task.card_job.strip().lower():
            tasks.append(task)
    for task in tasks:
        try:
            add_task_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-header/ion-toolbar/div/a[1]')
            add_task_btn.click()
            time.sleep(sleeping_time)
            __insert_task_name(browser,task)
            time.sleep(2)
            
            back_to_add_new_task = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-check-list-add-user/ion-header/ion-toolbar/ion-buttons/ion-icon')
            back_to_add_new_task.click()
            time.sleep(0.5)
        except Exception:
            print(Exception)
            continue
    browser.get("https://ionic.3i.com.vn/time-keeping") 
    time.sleep(4)
        
        
    
