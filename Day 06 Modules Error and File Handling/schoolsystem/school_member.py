

class SchoolMember:
    # class variable of school name
    school = 'Idrees Coding School'

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_info(self):
        print(f"Name: {self.name} | Role: {self.role} | School: {self.school}")

class Instructor(SchoolMember):
    def __init__(self, name, role, language):
        super().__init__(name, role)
        self.language = language

    def teach(self):
        print(f'{self.name} is now teaching {self.language}')

    def set_lanaguage(self, new_lanaguage):
        self.language = new_lanaguage

class HeadOfDepartment(SchoolMember):
    def __init__(self, name, role, department):
        super().__init__(name, role)
        self.department = department

    def get_deparment(self):
        print(f'{self.name} is now Head of the {self.department} Department')

    def set_department(self, new_department):
        self.department = new_department    

class Student(SchoolMember):
    def __init__(self, name, role, department, batch):
        super().__init__(name, role)
        self.department = department
        self.batch = self.batch

    def get_batch(self):
        print(f'{self.name} is fromt the {self.department}, started in year {self.batch}')

    def set_batch(self, new_batch):
        self.batch = new_batch     

def welcome_message():
    return "Welcome to the Staff Portal for Idrees Coding School"