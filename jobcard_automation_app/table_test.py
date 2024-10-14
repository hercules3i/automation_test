import time 
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
# from Task import TaskSimpleData
from selenium.common.exceptions import *
# from Bom import Warehouse
from datetime import datetime
sleeping_time = 0.25


def __selectBranch(browser,branch: str):
    # try:
        branch_element = browser.find_element(By.XPATH,
                                             '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-add-board/ion-content/div/div[2]/ion-item/ionic-selectable/div/button')
        branch_element.click()
        time.sleep(0.25)
        # search_element = browser.find_element(By.XPATH,'//*[@id="ion-overlay-17"]/ionic-selectable-modal/ion-header/ion-toolbar[2]/ion-searchbar/div/input')
        # search_element.send_keys(branch)
        time.sleep(sleeping_time)
        group_selection = browser.find_element(By.XPATH, '//*[@id="ion-overlay-3"]/ionic-selectable-modal/ion-content')
        group_selection.click()
        time.sleep(sleeping_time)
        all_branchs = group_selection.find_elements(By.TAG_NAME, 'ion-item')
        print("len:",len(all_branchs))
        time.sleep(0.25)

        for s in all_branchs:
            s_text = s.text
            if branch == s_text:
                s.click()
                break
    # except:
    #     raise Exception("__selectBranch()")

# def __selectDepartment(browser,department: str):
#     # try:
#         department = department.strip().lower()
#         print(department,len(department))
#         department_element = browser.find_element(By.XPATH,
#                                              '//*[@id="main-content"]/app-add-board/ion-content/div/div[4]/ion-item/ionic-selectable/div/button')
        
#         department_element.click()
#         time.sleep(0.25)
#         all_department= browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content')
#         all_department.click()
#         all_selection=all_department.find_elements(By.TAG_NAME,'ion-item')
#         print('len:',len(all_selection))
#         time.sleep(0.25)
#         for s in all_selection:
#             s_text = s.text
#             print(s_text,len(s_text))
#             if department == s_text.strip().lower():
#                 s.click()
#                 break
#     # # except:
#     # #     raise Exception("__selectDepartment()")


def __selectDepartment(browser, department: str):
    department = department.strip().lower()
    print(department, len(department))
    department_element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, 
            '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-add-board/ion-content/div/div[3]/ion-item/ionic-selectable/div/button'))
    )
    department_element.click()
    all_department = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, 
            '/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content'))
    )
    all_department.click()
    shadow_host = browser.find_element(By.TAG_NAME, 'ion-modal')
    shadow_root = browser.execute_script('return arguments[0].shadowRoot', shadow_host)
    item_groups = shadow_root.find_elements(By.TAG_NAME, 'ion-item-group')
    found = False
    for group in item_groups:
        all_items = group.find_elements(By.TAG_NAME, 'ion-item')
        for item in all_items:
            item_shadow_root = browser.execute_script('return arguments[0].shadowRoot', item)
            if item_shadow_root: 
                item_text = item_shadow_root.querySelector('div').innerText.strip().lower()  
                print(item_text, len(item_text))
                if department == item_text:
                    print(f"Clicking on: {item_text}")
                    browser.execute_script("arguments[0].click();", item)
                    found = True
                    break
        if found:
            break

    if not found:
        print("Department not found.")


# def __selectDepartment(browser, department: str):
#     department = department.strip().lower()
#     print(department, len(department))
#     department_element = WebDriverWait(browser, 10).until(
#         EC.element_to_be_clickable((By.XPATH, 
#             '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-add-board/ion-content/div/div[3]/ion-item/ionic-selectable/div/button'))
#     )
#     department_element.click()
#     all_department = WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.XPATH, 
#             '/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content'))
#     )
#     all_department.click()
#     shadow_host = browser.find_element(By.TAG_NAME, 'ion-modal')
#     shadow_root = browser.execute_script('return arguments[0].shadowRoot', shadow_host)
#     item_groups = shadow_root.find_elements(By.TAG_NAME, 'ion-item-group')
#     item_groups.click()
#     time.sleep(0.25)
#     found = False
#     for group in item_groups:
#         all_items = group.find_elements(By.TAG_NAME, 'ion-item')
#         for item in all_items:
#             s_text = item.text.strip().lower()
#             print(s_text, len(s_text))
#             if department == s_text:
#                 print(f"Clicking on: {s_text}")
#                 browser.execute_script("arguments[0].click();", item) 
#                 found = True
#                 break
#         if found:
#             break

#     if not found:
#         print("Department not found.")


# def __selectDepartment(browser, department: str):
#     # try:
#         department = department.strip().lower()
#         print(department, len(department))
#         department_element = browser.find_element(By.XPATH,
#             '//*[@id="main-content"]/app-add-board/ion-content/div/div[4]/ion-item/ionic-selectable/div/button')
        
#         department_element.click()
#         time.sleep(0.25) 
#         all_department = browser.find_element(By.CSS_SELECTOR, 'i')
#         all_department.click()
#         time.sleep(0.25)
#         group_xpaths = [
#             '/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list/ion-item-group[1]',  
#             '/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list/ion-item-group[2]', 
#             '/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list/ion-item-group[3]'   
#         ]
#         for group_xpath in group_xpaths:
#             item_group = browser.find_element(By.XPATH, group_xpath)
#             all_selection = item_group.find_elements(By.TAG_NAME, 'ion-item')
#             print(all_selection)
#             for s in all_selection:
#                 s_text = s.text.strip().lower() 
#                 print(s_text, len(s_text))
#                 if department == s_text:
#                     s.click()
#                     return 
#     # except Exception as e:
#     #     print(f"An error occurred: {e}")


def __selectTableType(browser,tab_type: str):
    # try:
        tab_type = tab_type.strip().lower()
        print(tab_type,len(tab_type))
        tab_type_element = browser.find_element(By.XPATH,
                                             '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-add-board/ion-content/div/div[4]/ion-item/ionic-selectable/div/button')
        tab_type_element.click()
        time.sleep(0.25)
        li_tab_type = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content')
        li_tab_type.click()
        all_tab_types = li_tab_type.find_elements(By.TAG_NAME, 'ion-item')
        print('len:',len(all_tab_types))
        for s in all_tab_types:
            s_text = s.text
            if tab_type == s_text.strip().lower():
                s.click()
                break
    # except:
    #     raise Exception("__selectTableType()")


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
    
def __finTableJob(browser, tables):
    list_app_elements = browser.find_element(By.XPATH, '//*[@id="main-content"]/app-time-keeping/ion-footer/app-menu-footer/div/div[2]/button')
    list_app_elements.click()
    time.sleep(0.15)
    tab_job_btn = browser.find_element(By.XPATH, '//*[@id="main-content"]/app-time-keeping/ion-footer/app-menu-footer/div[1]/div/div[3]/div')
    tab_job_btn.click()
    time.sleep(0.15)
    show_tabjobs_btn = browser.find_element(By.XPATH, '//*[@id="main-content"]/app-time-keeping/ion-content/div/div/div[1]/div/div[1]/label/i')
    show_tabjobs_btn.click()
    time.sleep(1)
            
    # Locate the table body element
    tbody_tabjob_element = browser.find_element(By.XPATH, '//*[@id="main-content"]/app-time-keeping/ion-content/div/div/div[1]/div/div[2]/div/table/tbody')
    tr_elements = tbody_tabjob_element.find_elements(By.TAG_NAME, "tr")
    existed_tables = []

    for i in range(1, len(tr_elements) + 1):
        # Find the second column of each row
        td_element = tbody_tabjob_element.find_element(By.XPATH, f'//*[@id="main-content"]/app-time-keeping/ion-content/div/div/div[1]/div/div[2]/div/table/tbody/tr[{i}]/td[2]')
        tab_job_name = td_element.text  # .text is an attribute, not a method
        existed_tables.append(tab_job_name)

    print(existed_tables)

    for new_table in tables:
        if new_table.name not in existed_tables:
            add_button = browser.find_element(By.XPATH, '//*[@id="main-content"]/app-time-keeping/ion-header/ion-toolbar/div/div/img')
            add_button.click()
            time.sleep(0.25)
            browser.refresh()
            time.sleep(3)
            
            name_input = browser.find_element(By.XPATH, '//*[@id="main-content"]/app-add-board/ion-content/div/div[1]/div/input')
            name_input.clear()
            name_input.send_keys(new_table.name)
            time.sleep(0.5)
            
            __selectBranch(browser,new_table.branch)
            time.sleep(0.5)
            
            __selectDepartment(browser,new_table.department)
            time.sleep(0.25)
            
            __selectTableType(browser,new_table.tab_type)
            time.sleep(0.25)
            
            # start_date = new_table.start_date.strftime('%d/%m/%Y')
            # __selectStartOrEndDate(browser,start_date, "start")
            # time.sleep(0.25)

            
            # end_date = new_table.end_date.strftime('%d/%m/%Y')
            # __selectStartOrEndDate(browser,end_date, "end")
            # time.sleep(0.25)
            # save_elements =browser.find_element(By.XPATH,'//*[@id="main-content-vatco"]/div[1]/div/div/div[3]/a')
            # save_elements.click()
            # time.sleep(0.75)