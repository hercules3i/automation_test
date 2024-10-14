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
sleeping_time = 0.25

def __select_staff(browser,task):
    pass
def __findToAddStaff(browser,task):
    add_staff_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-content/div/div[2]/div/div/ion-item/ion-row/ion-col[4]/i')
    add_staff_btn.click()
    time.sleep(sleeping_time)
    __select_staff(browser,task)
    

def __insert_task_name(browser, task):
    div_edit_content = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/div/ion-content/quill-editor/div/div[1]')
    div_edit_content.clear()
    div_edit_content.send_keys(task.name)
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
    add_task_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-header/ion-toolbar/div/a[1]')
    add_task_btn.click()
    time.sleep(sleeping_time)
    tasks = []
    for task in list_tasks:
        if jobCard_name.strip().lower() == task.card_job.strip().lower():
            tasks.append(task)
    for task in tasks:
        __insert_task_name(browser,task)
        
        
    
