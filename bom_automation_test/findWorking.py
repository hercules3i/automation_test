from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def __findWorking(nameTask: str, browser, delay: int):
    browser.implicitly_wait(delay)
    match nameTask:
        case "Công đoạn kéo":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[1]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Công đoạn dập và ren":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[2]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Nhiệt":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[3]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Xi mạ":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[4]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Đóng gói":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[5]/div/div/label/div/div/div/div/div/a/div/span').click()

list_workings = ["Xả tôn", "Ống gió",
                 "Cắt Laze", "Bọc Ei", "Phụ kiện ống gió","Chấn", "Hàn","Sơn","Lắp ráp","QA/QC"]

def __findWorkingFrige(nameTask: str, browser, delay: int):
    browser.implicitly_wait(delay)
    match nameTask:
        case "Xả tôn":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[1]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Ống gió":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[2]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Cắt Laze":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[3]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Bọc Ei":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[4]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Phụ kiện ống gió":
            browser.find_element(By.XPATH,
                                 '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[5]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Chấn":
            browser.find_element(By.XPATH,
                                '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[6]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Hàn":
            browser.find_element(By.XPATH,
                                '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[7]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Sơn":
            browser.find_element(By.XPATH,
                                '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[8]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "Lắp ráp":
            browser.find_element(By.XPATH,
                                '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[9]/div/div/label/div/div/div/div/div/a/div/span').click()
        case "QA/QC":
            browser.find_element(By.XPATH,
                                '//*[@id="contentMain"]/div[4]/div[3]/div/div[2]/div[10]/div/div/label/div/div/div/div/div/a/div/span').click()