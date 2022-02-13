from human import Human


class Student(Human):
    """Initialize Student class and extend Human class"""

    def __init__(self, name, surname, age, grade): # konstruktorius
        super().__init__(name, surname, age) # iskveciam human konstruktoriu
        self.grade = grade

    def get_student_info(self):

        self.get_human_info()
        print(f"Grade: \t\t{self.grade}")
