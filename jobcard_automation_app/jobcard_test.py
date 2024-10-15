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
from staff_test import __findToStaff
from task_test import __findToTasks
sleeping_time = 0.25
import logging
from log import logger
# Tạo logger chung

def __selectWorkflow(browser, workflow):
    workflow = (workflow.strip()).lower()
    workflow_btn = browser.find_element(By.XPATH,'//*[@id="main-content"]/app-create-card-job/ion-content/div/div[3]/div[2]/div[8]/ion-item/ionic-selectable/div/button')
    workflow_btn.click()
    time.sleep(1)
    workflow_father_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list/ion-item-group')
    group_workflow_span = workflow_father_element.find_elements(By.CSS_SELECTOR,'[class="product-name ng-star-inserted"]')
    found = False  

    for element in group_workflow_span:
        element_text = (element.text).strip().lower()
        print(f"Element text: '{element_text}', Workflow: '{workflow}'")
        
        if element_text == workflow:
            browser.execute_script("arguments[0].click();", element)
            time.sleep(sleeping_time)
            found = True  # Đánh dấu là đã tìm thấy workflow
            break

    if not found:
        print("Không có workflow nào thỏa mãn.")
        logger.warning("Khong co workflow nao thoa man.")
        close_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-header/ion-toolbar[1]/ion-buttons/ion-button')
        close_btn.click()
        time.sleep(sleeping_time)

        
        

def __save(browser):
    save_btn = browser.find_element(By.XPATH,'//*[@id="main-content"]/app-create-card-job/ion-header/ion-toolbar/div')
    save_btn.click()
    print("saving....")
    try:
            toast_container = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-toast').shadow_root
            message = toast_container.find_element(By.CLASS_NAME, 'toast-message').text
            message = message.split(" ")
            if "thành công" in message:
                logger.info(message)
            else:
                logger.warning(message)
    except NoSuchElementException as e:
            logger.error(f"Element not found: {e}")
    except Exception as e:
            logger.error(f"An error occurred: {e}", exc_info=True)

    time.sleep(5)
    print("done....")
    

def __selectCardStatus(browser, card_status):
    try:
        card_status = (card_status.strip()).lower()
        card_status_btn = browser.find_element(By.XPATH,'//*[@id="main-content"]/app-create-card-job/ion-content/div/div[3]/div[2]/div[7]/ion-item/ionic-selectable/div/button')
        card_status_btn.click()
        time.sleep(sleeping_time)
        card_status_father_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list/ion-item-group')
        group_card_status_label = card_status_father_element.find_elements(By.TAG_NAME,'ion-label')
        for element in group_card_status_label:
            print(((element.text).strip()).lower(), card_status)
            if ((element.text).strip()).lower() == card_status:
                element.click()
                break
    except Exception:
        logger.warning(f"Khòn co status nao thoa man {card_status}")


def __selectJobType(browser, job_type):
    try:
        job_type = (job_type.strip()).lower()
        job_type_btn = browser.find_element(By.XPATH,'//*[@id="main-content"]/app-create-card-job/ion-content/div/div[3]/div[2]/div[6]/ion-item/ionic-selectable/div/button')
        job_type_btn.click()
        time.sleep(sleeping_time)
        job_type_father_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list/ion-item-group')
        group_job_type_label = job_type_father_element.find_elements(By.TAG_NAME,'ion-label')
        for element in group_job_type_label:
            print(((element.text).strip()).lower(), job_type)
            if ((element.text).strip()).lower() == job_type:
                element.click()
                break
    except Exception:
        logger.warning(f"Khong co kieu cong viec {job_type}")

# select priority
def __selectPriority(browser,priority):
    try:
        
        priority = (priority.strip()).lower()
        priority_btn = browser.find_element(By.XPATH,'//*[@id="main-content"]/app-create-card-job/ion-content/div/div[3]/div[2]/div[5]/ion-item/ionic-selectable/div/button')
        priority_btn.click()
        time.sleep(sleeping_time)
        priority_father_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list/ion-item-group')
        group_priority_label = priority_father_element.find_elements(By.TAG_NAME,'ion-label')
        for element in group_priority_label:
            print(((element.text).strip()).lower(), priority)
            if ((element.text).strip()).lower() == priority:
                element.click()
                break
    except Exception as e:
        print(e)
        logger.warning(f"Khong co do uu tien {priority}")
        logger.error(e)
def __selectStartOrEndDate(browser,date: dict,type):

    str_date = str(date)
    print(str_date)
    if type == "start":
        date_element = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-content/div/div[3]/div[2]/div[2]/div/smart-datetime/button')
    else:
        date_element = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-content/div/div[3]/div[2]/div[3]/div/smart-datetime/button')
            
    date_element.click()
    time.sleep(1)
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
    test = ion_datetime_shadow.find_element(By.CSS_SELECTOR,'[class="calendar-month-year"]')
    ion_item_ele = test.find_element(By.TAG_NAME,'ion-item')
    ion_label_btn = ion_item_ele.find_element(By.TAG_NAME,'ion-label')
    ion_label_btn.click()
    time.sleep(0.5)
    group_month_element = ion_datetime_shadow.find_element(By.CSS_SELECTOR,'[class="month-column ion-color ion-color-primary md hydrated"]').shadow_root
    list_month_btn = group_month_element.find_elements(By.CSS_SELECTOR, '[class="picker-item"]')
    selected_month = group_month_element.find_element(By.CSS_SELECTOR, '[class="picker-item picker-item-active"]')

    browser.execute_script("arguments[0].classList.remove('picker-item-active');", selected_month)

    for element in list_month_btn:
        if date['month'].lower() == element.text.lower():
            browser.execute_script("arguments[0].classList.add('picker-item-active');", element)
            print(f"Updated: {element.text}")
            break
    time.sleep(sleeping_time)
    group_year_element = ion_datetime_shadow.find_element(By.CSS_SELECTOR,'[class="year-column ion-color ion-color-primary md hydrated"]').shadow_root
    list_year_btn = group_year_element.find_elements(By.CSS_SELECTOR,'[class="picker-item"]')
    selected_year = group_year_element.find_element(By.CSS_SELECTOR,'[class="picker-item picker-item-active"]')
    print(len(list_year_btn), selected_year.text)


    for element in list_year_btn:
        print(element.text, date['year'])
        if date['year'] == element.text:
            browser.execute_script("arguments[0].classList.remove('picker-item-active');", selected_year)

            browser.execute_script("arguments[0].classList.add('picker-item-active');", element)
            print(f"Updated: {element.text}")
            break
    time.sleep(sleeping_time)
    ok_element = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/div/ion-header/ion-toolbar/ion-buttons[2]')
    ok_element.click()
        



def __select_tabjob(browser, tabjob_name):
    tabjob_selection_ele = browser.find_element(By.XPATH,'//*[@id="main-content"]/app-create-card-job/ion-content/div/div[1]/ion-item/ionic-selectable/div/button')
    tabjob_selection_ele.click()
    time.sleep(0.5)
    group_selection_tabjob = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list/ion-item-group')
    
    list_selection_tabjob = group_selection_tabjob.find_elements(By.TAG_NAME,'ion-label')
    for element in list_selection_tabjob:
        print(element.text)
        element.click()
        time.sleep(0.5)
        break
        if tabjob_name == element.text:
            element.click()
            break
    list_job_ele = browser.find_element(By.XPATH,'//*[@id="main-content"]/app-create-card-job/ion-content/div/div[2]/ion-item/ionic-selectable/div/button')
    list_job_ele.click()
    time.sleep(0.5)
    group_selection_list_tabjob = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list/ion-item-group')
    
    list_selection_list_tabjob = group_selection_list_tabjob.find_elements(By.TAG_NAME,'ion-label')
    for element in list_selection_list_tabjob:
        print(element.text)
        element.click()
        time.sleep(0.5)
        break
        if tabjob_name == element.text:
            element.click()
            break
    move_to_add_job_card_ele = browser.find_element(By.XPATH, "/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-content/div/div[3]/i")
    move_to_add_job_card_ele.click()
    time.sleep(0.25)

def __finJobCard(browser,list_jobcards,list_staffs,list_tasks):

    for i in range(9,len(list_jobcards)):
        count_case = i
        count_error = 0
        try:
            time.sleep(0.25)
            add_jobcard_element =  browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-time-keeping/ion-header/ion-toolbar/div/div/a[1]')
            add_jobcard_element.click()

            time.sleep(sleeping_time)
            browser.refresh()
            time.sleep(3)
            __select_tabjob(browser, list_jobcards[i].tab_job)
            time.sleep(0.5)
            if list_jobcards[i].name is None:
                i = 2
            cardname_input = browser.find_element(By.XPATH,"/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-content/div/div[1]/div/input")
            print(list_jobcards[i].name)
            cardname_input.clear()
            cardname_input.send_keys(list_jobcards[i].name)

            start_date = list_jobcards[i].start_date

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
            end_date = list_jobcards[i].end_date

            day = end_date.strftime('%d') 
            month = end_date.strftime('%B')  # Lấy tháng dưới dạng tên tiếng Anh đầy đủ
            year = end_date.strftime('%Y') 
            end_date_compile = {
                "day":day,
                "month":month,
                "year":year
            }
            print(end_date_compile)
            try:
                __selectStartOrEndDate(browser, end_date_compile, "end")
            except Exception as e:
                logger.error(f"{list_jobcards[i].name} - Lỗi khi chọn ngày kết thúc cho jobcard {list_jobcards[i].name}: {e}", exc_info=True)
                browser.get("https://ionic.3i.com.vn/time-keeping")
                time.sleep(1)
                continue  # Tiếp tục vòng lặp nếu có lỗi

            time.sleep(0.25)

            try:
                __selectPriority(browser, list_jobcards[i].priority)
            except Exception as e:
                logger.error(f"{list_jobcards[i].name} - Lỗi khi chọn mức độ ưu tiên cho jobcard {list_jobcards[i].name}: {e}", exc_info=True)
                browser.get("https://ionic.3i.com.vn/time-keeping")
                time.sleep(1)
                continue  # Tiếp tục vòng lặp nếu có lỗi

            time.sleep(sleeping_time)

            try:
                __selectJobType(browser, list_jobcards[i].job_type)
            except Exception as e:
                logger.error(f"{list_jobcards[i].name} - Lỗi khi chọn loại công việc cho jobcard {list_jobcards[i].name}: {e}", exc_info=True)
                browser.get("https://ionic.3i.com.vn/time-keeping")
                time.sleep(1)
                continue  # Tiếp tục vòng lặp nếu có lỗi

            time.sleep(sleeping_time)

            try:
                __selectCardStatus(browser, list_jobcards[i].card_status)
            except Exception as e:
                logger.error(f"{list_jobcards[i].name} - Lỗi khi chọn trạng thái thẻ cho jobcard {list_jobcards[i].name}: {e}", exc_info=True)
                browser.get("https://ionic.3i.com.vn/time-keeping")
                time.sleep(1)
                continue  # Tiếp tục vòng lặp nếu có lỗi

            time.sleep(sleeping_time)

            try:
                __save(browser)
            except Exception as e:
                logger.error(f"{list_jobcards[i].name} - Lỗi khi lưu jobcard {list_jobcards[i].name}: {e}", exc_info=True)
                browser.get("https://ionic.3i.com.vn/time-keeping")
                time.sleep(1)
                continue  # Tiếp tục vòng lặp nếu có lỗi

            time.sleep(sleeping_time)

            try:
                __selectWorkflow(browser, list_jobcards[i].workflow)
            except Exception as e:
                logger.error(f"{list_jobcards[i].name} - Lỗi khi chọn luồng công việc cho jobcard {list_jobcards[i].name}: {e}", exc_info=True)
                browser.get("https://ionic.3i.com.vn/time-keeping")
                time.sleep(1)
                continue  # Tiếp tục vòng lặp nếu có lỗi

            time.sleep(sleeping_time)

            try:
                __save(browser)
            except Exception as e:
                logger.error(f"{list_jobcards[i].name} - Lỗi khi lưu luồng công việc cho jobcard {list_jobcards[i].name}: {e}", exc_info=True)
                browser.get("https://ionic.3i.com.vn/time-keeping")
                time.sleep(1)
                continue  # Tiếp tục vòng lặp nếu có lỗi

            time.sleep(sleeping_time)

            try:
                __findToStaff(browser, list_staffs, list_jobcards[i].name, list_tasks)
            except Exception as e:
                logger.error(f"{list_jobcards[i].name} - Lỗi khi tìm nhân viên cho jobcard {list_jobcards[i].name}: {e}", exc_info=True)
                browser.get("https://ionic.3i.com.vn/time-keeping")
                time.sleep(1)
                continue  # Tiếp tục vòng lặp nếu có lỗi



        except Exception as e:
            logger.error(f"{list_jobcards[i].name} - An error occurred: {e}", exc_info=True)
            if count_error == 2:
                browser.get("https://ionic.3i.com.vn/time-keeping")
                time.sleep(1)
                continue
            
            count_error+=1
            i = i - 1
            
    
