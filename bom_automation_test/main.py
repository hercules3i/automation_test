from Excel import LoadSimpleData
from Automation_test import AutoTest

if __name__ == '__main__':
    list_tasks = LoadSimpleData()
    AutoTest(list_tasks)
