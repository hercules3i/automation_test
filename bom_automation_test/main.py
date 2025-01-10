from Excel import LoadSimpleData,LoadExtendedData
from Automation_test import AutoTest

if __name__ == '__main__':
    list_tasks = LoadExtendedData()
    AutoTest(list_tasks)
