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
from log import logger
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



def __selectDepartment(browser, department):
    try:
        list_departments = []
        list_departments.append(department)
        # Cập nhật các phần tử của list_departments
        for i in range(len(list_departments)):
            list_departments[i] = list_departments[i].strip().lower()
            if list_departments[i] == None or list_departments[i] == "":
                list_departments[i] == "tất cả người dùng"
        print(str(list_departments))
        # Tìm nút "display_departments_btn" trên giao diện web
        display_departments_btn = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-add-board/ion-content/div/div[3]/ion-item/ionic-selectable/div/button')
        display_departments_btn.click()
        time.sleep(0.5)
        while True:
            try:
                father_group_choices = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list')
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
        logger.warning(f"{department} - Khong co phong ban nhom nao thoa man {str(list_departments)}")



def __selectTableType(browser,tab_type: str):
    # try:
        display_all_selections = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-add-board/ion-content/div/div[4]/ion-item/ionic-selectable/div/button')
        display_all_selections.click()
        time.sleep(sleeping_time)
        tab_type = tab_type.strip().lower()
        print(tab_type,len(tab_type))
        tab_type_group = browser.find_element(By.XPATH,
                                             '/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list')
        time.sleep(0.25)
        ion_label_tab_type = tab_type_group.find_elements(By.TAG_NAME, 'ion-label')
        print('len:',len(ion_label_tab_type))
        for s in ion_label_tab_type:
            s_text = s.text
            if tab_type == s_text.strip().lower():
                s.click()
                break
    # except:
    #     raise Exception("__selectTableType()")

def __selectStartOrEndDate(browser,date: dict,type):

    str_date = str(date)
    print(str_date)
    if type == "start":
        date_element = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-add-board/ion-content/div/div[6]/div[1]/div/smart-datetime/button')
    else:
        date_element = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-add-board/ion-content/div/div[6]/div[2]/div/smart-datetime/button')
            
    date_element.click()
    time.sleep(1.5)
    ion_datetime_shadow = browser.find_element(By.TAG_NAME,'ion-datetime').shadow_root

    # select day
    next_month_btn = ion_datetime_shadow.find_element(By.CSS_SELECTOR,'[class="calendar-next-prev"]')

    ion_button_ele = next_month_btn.find_elements(By.TAG_NAME,'ion-button')
    print(ion_button_ele[0].tag_name)
    ion_button_ele[1].click()
    time.sleep(sleeping_time)
    group_day_dad_ele = ion_datetime_shadow.find_element(By.CSS_SELECTOR,'[class="calendar-month-grid"]')
    list_days_btn = group_day_dad_ele.find_elements(By.TAG_NAME, 'button')
    print(len(list_days_btn))
    for element in list_days_btn:
        print(f"Element text: '{element.text}', Expected day: {int(date['day'])}")
        
        # Kiểm tra nếu element.text rỗng hoặc không phải số
        if element.text == None or element.text == '':
            print(f"Skipping invalid element with text: '{element.text}'")
            continue
        else:
        # So sánh giá trị của element.text với ngày
            try:
                if int(element.text) == int(date['day']):
                    print(f"Clicking element with tag: {element.tag_name}")
                    
                    # Thực hiện click bằng JavaScript
                    browser.execute_script("arguments[0].click();", element)
                    time.sleep(sleeping_time)
                    break
            except Exception as e:
                print(e)
                continue

    # select month and year
    time.sleep(2)
    test = ion_datetime_shadow.find_element(By.CSS_SELECTOR,'[class="calendar-month-year"]')
    ion_item_ele = test.find_element(By.TAG_NAME,'ion-item')
    ion_label_btn = ion_item_ele.find_element(By.TAG_NAME,'ion-label')
    ion_label_btn.click()
    time.sleep(0.5)

    group_year_element = ion_datetime_shadow.find_element(By.CSS_SELECTOR,'[class="year-column ion-color ion-color-primary md hydrated"]').shadow_root
    list_year_btn = group_year_element.find_elements(By.CSS_SELECTOR,'[class="picker-item"]')
    selected_year = group_year_element.find_element(By.CSS_SELECTOR,'[class="picker-item picker-item-active"]')
    print(len(list_year_btn), selected_year.text)

    for element in list_year_btn:
        print(element.text, date['year'])
        if date['year'] == element.text:
            
            browser.execute_script("arguments[0].classList.remove('picker-item-active');", selected_year)

            browser.execute_script("arguments[0].classList.add('picker-item-active');", element)
            browser.execute_script("arguments[0].click();", element)

            print(f"Updated: {element.text}")
            break
    time.sleep(3)
    group_month_element = ion_datetime_shadow.find_element(By.CSS_SELECTOR,'[class="month-column ion-color ion-color-primary md hydrated"]').shadow_root
    list_month_btn = group_month_element.find_elements(By.CSS_SELECTOR, '[class="picker-item"]')
    selected_month = group_month_element.find_element(By.CSS_SELECTOR, '[class="picker-item picker-item-active"]')

    for element in list_month_btn:
        print(date['month'].lower(),element.text.lower())
        if date['month'].lower() == element.text.lower():
            browser.execute_script("arguments[0].classList.remove('picker-item-active');", selected_month)

            browser.execute_script("arguments[0].classList.add('picker-item-active');", element)
            browser.execute_script("arguments[0].click();", element)
            print(f"Updated: {element.text}")
            break

    time.sleep(3)
    ok_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/div/ion-header/ion-toolbar/ion-buttons[2]')
    ok_element.click()
        

    
def __finTableJob(browser, tables):

    for new_table in tables:
        list_app_elements = browser.find_element(By.XPATH, '//*[@id="main-content"]/app-time-keeping/ion-footer/app-menu-footer/div/div[2]/button')
        list_app_elements.click()
        time.sleep(0.25)
        tab_job_btn = browser.find_element(By.XPATH, '//*[@id="main-content"]/app-time-keeping/ion-footer/app-menu-footer/div[1]/div/div[3]/div')
        tab_job_btn.click()
        time.sleep(0.25)
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
            start_date = new_table.start_date

            day = start_date.strftime('%d') 
            month = start_date.strftime('%B')  # Lấy tháng dưới dạng tên tiếng Anh đầy đủ
            year = start_date.strftime('%Y') 
            start_date_compile = {
                "day":day,
                "month":month,
                "year":year
            }
            
            __selectStartOrEndDate(browser,start_date_compile, "start")
            time.sleep(1)
            end_date = new_table.end_date

            day = end_date.strftime('%d') 
            month = end_date.strftime('%B')  # Lấy tháng dưới dạng tên tiếng Anh đầy đủ
            year = end_date.strftime('%Y') 
            end_date_compile = {
                "day":day,
                "month":month,
                "year":year
            }
            print(end_date_compile)
            __selectStartOrEndDate(browser, end_date_compile, "end")
            time.sleep(sleeping_time)
            save_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-add-board/ion-header/ion-toolbar/div/i')
            save_btn.click()
            time.sleep(0.5)
            browser.get("https://ionic.3i.com.vn/time-keeping")
            time.sleep(2)

            