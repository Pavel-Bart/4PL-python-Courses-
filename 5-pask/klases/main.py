from human import Human
from student import Student

vardenis = Human("Paulius", "Pauliauskas", 44)
#vardenis.get_human_info()
vardenis.change_human("qq", "qq", 23)
vardenis.get_human_info()

vardenis = Student("Paulius", "Pauliauskas", 44, 9)
# vardenis.get_student_info()
print("----------------------------")
vardenis = Human("Arturas", "Arturskas", 44)
vardenis.get_human_info()

