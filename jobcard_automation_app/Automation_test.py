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
from table_test import __finTableJob
from jobcard_test import __finJobCard
options = Options()
options.add_experimental_option("detach", True)

browser = Chrome(options)
browser.maximize_window()
actionChains = ActionChains(browser)
link = "https://ionic.3i.com.vn/login"
username = "admin"
password = "winwin2021"
code = "vft"


delay = 10
sleeping_time = 0.25


def __login():
    browser.find_element(By.XPATH, '//*[@id="main-content"]/app-login/ion-content/div/button/i').click()
    time.sleep(0.15)
    browser.find_element(By.XPATH, '//*[@id="main-content"]/app-login/ion-content/div/div[1]/ion-input/input').send_keys(code)
    browser.find_element(By.XPATH, '//*[@id="main-content"]/app-login/ion-content/div/div[3]/ion-row/div/div[1]/div[1]/ion-input/input').send_keys(username)
    browser.find_element(By.XPATH, '//*[@id="main-content"]/app-login/ion-content/div/div[3]/ion-row/div/div[1]/div[2]/ion-input/input').send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="main-content"]/app-login/ion-content/div/div[3]/ion-row/div/button').click()

def __findToJobCard():
    
    add_card_element =  browser.find_element(By.XPATH, '//*[@id="main-content"]/app-dash-board/ion-content/div/div[1]/div[1]/div[1]/i')
    add_card_element.click()
    time.sleep(1)


def AutoTest(tasks: list):
    
    browser.get(link)
    __login()
    time.sleep(3)
    __findToJobCard()
    # __finTableJob(browser,tasks["list_tabjobs"])
    time.sleep(1.5)
    __finJobCard(browser,tasks["list_jobcards"],tasks["list_staffs"],tasks["list_tasks"])
    time.sleep(sleeping_time)
    
    
    