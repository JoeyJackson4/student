class Student():
    def __init__(self,fname,lname,age,grade):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.grade = grade
        self.classes = {}
    def add_class(self,class_name):
        self.classes[class_name] = None
    def add_final_grade(self, class_name,final_grade):
        self.class_name = class_name
        self.final_grade = final_grade
        if class_name in self.classes:
            self.classes[class_name] = final_grade
        else:
            print("class name does not exist.")
    def average_grade(self,class_number,grade1,grade2,grade3,grade4):
        self.class_number =  class_number
        self.grade1 =  grade1
        self.grade2 =  grade2
        self.grade3 =  grade3
        self.grade4 =  grade4
        average = grade1+grade2+grade3+grade4
        average_grade = average//class_number
        print(average_grade)