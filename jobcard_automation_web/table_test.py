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


def __selectBranch(browser,branch: str):
    try:
        branch_element = browser.find_element(By.XPATH,
                                             '//*[@id="modal-body"]/div/form/div/div[2]/div/div/div[1]/span')
        branch_element.click()
        time.sleep(sleeping_time)
        li_branch = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/form/div/div[2]/div/div/ul/li')
        time.sleep(sleeping_time)
        all_branchs = li_branch.find_elements(By.TAG_NAME, 'a')
        
        time.sleep(sleeping_time)

        for s in all_branchs:
            s_text = s.text
            if branch == s_text:
                s.click()
                break
    except:
        raise Exception("__selectBranch()")

def __selectDepartment(browser,department: str):
    try:
        department = department.strip().lower()
        print(department,len(department))
        department_element = browser.find_element(By.XPATH,
                                             '//*[@id="modal-body"]/div/form/div/div[3]/div/div/div[1]/span')
        
        department_element.click()
        time.sleep(sleeping_time)
        li_department = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/form/div/div[3]/div/div/ul/li')
        time.sleep(sleeping_time)
        all_departments = li_department.find_elements(By.TAG_NAME, 'a')
        
        time.sleep(sleeping_time)

        for s in all_departments:
            s_text = s.text
            print(s_text,len(s_text))
            if department == s_text.strip().lower():
                s.click()
                break
    except:
        raise Exception("__selectDepartment()")
def __selectTableType(browser,tab_type: str):
    try:
        tab_type = tab_type.strip().lower()
        tab_type_element = browser.find_element(By.XPATH,
                                             '//*[@id="modal-body"]/div/form/div/div[4]/div[1]/div/div[1]/span')
        tab_type_element.click()
        time.sleep(sleeping_time)
        li_tab_type = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/form/div/div[4]/div[1]/div/ul/li')
        time.sleep(sleeping_time)
        all_tab_types = li_tab_type.find_elements(By.TAG_NAME, 'a')
        
        time.sleep(sleeping_time)

        for s in all_tab_types:
            s_text = s.text
            if tab_type == s_text.strip().lower():
                s.click()
                break
    except:
        raise Exception("__selectTableType()")

def __selectStartOrEndDate(browser,date: str,type):
    try:
        if type == "start":
            date_element = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/form/div/div[5]/div[1]/div/input')
        else:
            date_element = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/form/div/div[5]/div[2]/div/input')
            
        date = date.strip()           
        date_element.click()
        time.sleep(sleeping_time)
        date_element.send_keys(date)
    except:
        raise Exception("__selectStartOrEndDate()")
    
def __finTableJob(browser,tables):
    
    tab_job_exists = browser.find_elements(By.XPATH, '//*[@id="list-board"]//b[@class="ng-binding"]')
    existed_tables = []
    for b in tab_job_exists:
        existed_tables.append(b.text)
    for new_table in tables:
        if new_table.name not in existed_tables:
            add_button = browser.find_element(By.XPATH, '//*[@id="list-board"]/div[1]/div/div/span/a/span/i')
            add_button.click()
            time.sleep(0.5)
            
            name_input = browser.find_element(By.XPATH, '//*[@id="modal-body"]/div/form/div/div[1]/div/input')
            name_input.clear()
            name_input.send_keys(new_table.name)
            time.sleep(0.5)
            
            __selectBranch(browser,new_table.branch)
            time.sleep(0.5)
            
            __selectDepartment(browser,new_table.department)
            time.sleep(0.25)
            
            __selectTableType(browser,new_table.tab_type)
            time.sleep(0.25)
            
            start_date = new_table.start_date.strftime('%d/%m/%Y')
            __selectStartOrEndDate(browser,start_date, "start")
            time.sleep(0.25)

            
            end_date = new_table.end_date.strftime('%d/%m/%Y')
            __selectStartOrEndDate(browser,end_date, "end")
            time.sleep(0.25)
            save_elements =browser.find_element(By.XPATH,'//*[@id="main-content-vatco"]/div[1]/div/div/div[3]/a')
            save_elements.click()
            time.sleep(0.75)
            
