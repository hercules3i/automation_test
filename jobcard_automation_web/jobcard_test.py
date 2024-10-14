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

def __finJobCard(browser,jobcards):
    assign_work_elements =  browser.find_elements(By.XPATH, '//*[@id="BoardDetail"]/div[1]/div[2]/div/div[2]/a/i')
    assign_work_elements.click()
