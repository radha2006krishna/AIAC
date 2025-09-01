class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "Fail"
        self.display()
print("Enter student details:")
name = input("Name: ")
roll_no = input("Roll No: ")
marks = float(input("Marks: "))
student1 = student(name, roll_no, marks)
student1.display()