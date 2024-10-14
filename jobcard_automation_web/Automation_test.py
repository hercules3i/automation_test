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
options = Options()
options.add_experimental_option("detach", True)

browser = Chrome(options)
browser.maximize_window()
actionChains = ActionChains(browser)
link = "https://os.3i.com.vn/Admin/Account/Login?ReturnUrl=%2FAdmin"
username = "admin"
password = "winwin2021"


delay = 10
sleeping_time = 0.25


def __login():
    browser.find_element(By.ID, "UserName").send_keys(username)
    browser.find_element(By.ID, "Password").send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="true_inner"]/section/form/div[3]/button').click()

def __findToJobCard():
    # browser.get("https://vft.appsmartwork.com/Admin/Bom#/")
    browser.get("https://os.3i.com.vn/Admin/CardJob#/")
    # WebDriverWait(browser, delay).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="contentMain"]/div/div/div/ul/li[1]'))
    # ).click()
            

def AutoTest(tasks: list):
    
    browser.get(link)
    __login()
    __findToJobCard()
    time.sleep(5)
    __finTableJob(browser,tasks["list_tabjobs"])
    time.sleep(2)
    # __findJobCard((browser,tasks["list_tabjobs"])