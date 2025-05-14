from student import Student

student1 = Student("Emma", "Sun", 15, "10th")


error = True
student1.add_class("Physics")
student1.add_class("English")
student1.add_class("Computer Science")

for i in range(1,4):
    classs = input("enter your class name: ")
    grade = int(input("enter your grade: "))
    student1.add_final_grade
    if classs in student1.classes: 
        if grade ==int and grade<100:       
            student1.add_final_grade(classs,grade)
        else:
            error = True
            while error == True:
                grade = input("(invalid input)enter your grade: ")
                if grade == int and grade<101:
                    if classs in student1.classes:        
                        student1.add_final_grade(classs,grade)
                        error = False
    elif grade !=int and grade>100:
        error = True
        while error == True:
            grade = input("(invalid input)enter your grade: ")
            if grade == int and grade<101:
                if classs in student1.classes:        
                    student1.add_final_grade(classs,grade)
                    error = False
                else:
                    error = True
                    while error == True:
                        classs = input("(not a vaild class)enter your class name: ")
                        if classs in student1.classes:
                            student1.add_final_grade(classs,grade)
                            error = False
    else:
        error = True
        while error == True:
            classs = input("(not a vaild class)enter your class name: ")
            if classs in student1.classes:
                student1.add_final_grade(classs,grade)
                error = False


print("Student Name: "+student1.fname+" "+student1.lname)
print("Age: "+str(student1.age))
print("Grade: "+student1.grade)
print("Classes: ")
print(student1.classes)

classn = int(input("enter the amount of classes you have: "))
grad1 = int(input("enter the amount of grade for your first class: "))
grad2 = int(input("enter the amount of grade for your second class: "))
grad3 = int(input("enter the amount of grade for your third class: "))
grad4 = int(input("enter the amount of grade for your fourth class: "))
student1.average_grade(classn,grad1,grad2,grad3,grad4)

