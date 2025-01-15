from Excel import LoadSimpleData
from Automation_test import AutoTest
import openpyxl
import os
if __name__ == '__main__':
    list_tasks = LoadSimpleData()
    AutoTest(list_tasks)
