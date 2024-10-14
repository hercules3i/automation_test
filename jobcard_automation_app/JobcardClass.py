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
    def __init__(self, card_name, start_date, end_date, card_status,weight,tab_job,category_job,priority,job_type, funding,money_type,cycle,workflow):
        super().__init__(card_name)  
        self.start_date = start_date
        self.end_date = end_date
        self.card_status = card_status
        self.weight = weight
        self.tab_job = tab_job
        self.category_job = category_job
        self.priority = priority
        self.job_type = job_type
        self.funding = funding
        self.money_type = money_type
        self.cycle = cycle
        self.workflow = workflow
        

    def get_info(self):
        info = (
            f"+----------------+-----------------------------+\n"
            f"| Field          | Value                       |\n"
            f"+----------------+-----------------------------+\n"
            f"| Name           | {self.name}                 |\n"
            f"| Start Date     | {self.start_date}           |\n"
            f"| End Date       | {self.end_date}             |\n"
            f"| Status         | {self.card_status}          |\n"
            f"| Weight         | {self.weight}               |\n"
            f"| Tab Job        | {self.tab_job}              |\n"
            f"| Category Job   | {self.category_job}         |\n"
            f"| Priority       | {self.priority}             |\n"
            f"| Job Type       | {self.job_type}             |\n"
            f"| Funding        | {self.funding}              |\n"
            f"| Money Type     | {self.money_type}           |\n"
            f"| Cycle          | {self.cycle}                |\n"
            f"| Workflow       | {self.workflow}             |\n"
            f"+----------------+-----------------------------+"
        )
        return info

    def __str__(self):
        return f"CardJob({self.name}, {self.start_date} - {self.end_date}, Status: {self.card_status})"


class Staff():
    def __init__(self,card_job, branch_agency, department_group,list_staffs):
        self.list_staffs = list_staffs
        self.card_job = card_job
        self.branch_agency = branch_agency
        self.department_group = department_group


    def get_info(self):
        info = (
            f"+-------------------+--------------------------+\n"
            f"| Field             | Value                    |\n"
            f"+-------------------+--------------------------+\n"
            f"| Staff Name        | {self.name}              |\n"
            f"| Card Job          | {self.card_job}          |\n"
            f"| Branch Agency     | {self.branch_agency}     |\n"
            f"| Department Group  | {self.department_group}  |\n"
            f"+-------------------+--------------------------+"
        )
        return info
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
        info = (
            f"+-------------------+--------------------------+\n"
            f"| Field             | Value                    |\n"
            f"+-------------------+--------------------------+\n"
            f"| Task Name         | {self.task_name}          |\n"
            f"| Card Job          | {self.card_job}          |\n"
            f"| Weight            | {self.weight}            |\n"
            f"| Assigned Staff    | {self.staff}             |\n"
            f"| Duration          | {self.duration} {self.unit} |\n"
            f"+-------------------+--------------------------+"
        )
        return info
