from abc import ABC, abstractmethod
class JobCard(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_info(self):
        pass

    def __str__(self):
        return f"JobCard({self.name})"

class TabJob(JobCard):
    def __init__(self, tab_name, branch, department, tab_type, start_date, end_date):
        super().__init__(tab_name) 
        self.branch = branch
        self.department = department
        self.tab_type = tab_type
        self.start_date = start_date
        self.end_date = end_date
    def get_info(self):
        return f"TabJob({self.name}, {self.branch}, {self.department}, {self.tab_type})"

    def __str__(self):
        return f"TabJob({self.name}, {self.branch}, {self.department}, {self.tab_type}, {self.start_date} - {self.end_date})"


class CardJob(JobCard):
    def __init__(self, card_name, start_date, end_date, card_status,weight,tab_job,category_job):
        super().__init__(card_name)  
        self.start_date = start_date
        self.end_date = end_date
        self.card_status = card_status
        self.weight = weight
        self.staffs = []
        self.tab_job = tab_job
        self.category_job = category_job


    def get_info(self):
        return f"CardJob({self.name}, {self.start_date} - {self.end_date}, Status: {self.card_status}"

    def __str__(self):
        return f"CardJob({self.name}, {self.start_date} - {self.end_date}, Status: {self.card_status})"


class Staff(JobCard):
    def __init__(self,card_job, branch_agency, department_group, staff_name):
        super().__init__(staff_name)  
        self.card_job = card_job
        self.branch_agency = branch_agency
        self.department_group = department_group
        self.tasks = []


    def get_info(self):
        return f"Staff(Staff: {self.name}, Agency: {self.branch_agency}, Group: {self.department_group}"
    def __str__(self):
        return f"Staff(Staff: {self.name}, Agency: {self.branch_agency}, Group: {self.department_group})"



class Task(JobCard):
    def __init__(self,card_job, task_name, weight,staff, duration, unit):
        super().__init__(task_name)  
        self.card_job = card_job
        self.task_name = task_name
        self.weight = weight
        self.staff = staff
        self.duration = duration
        self.unit = unit

    def __str__(self):
        return f"Task({self.name}, Weight: {self.weight}, Duration: {self.duration})"
    def get_info(self):
        return f"Task({self.name}, Weight: {self.weight}, Duration: {self.duration})"
