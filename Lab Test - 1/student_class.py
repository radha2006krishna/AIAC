class Student:
    GRADE_BANDS = {
        "A+": (90, 100),
        "A": (75, 89),
        "B": (60, 74),
        "C": (50, 59),
        "F (Fail)": (0, 49),
    }
    def __init__(self, name: str, roll_no, marks: float) -> None:
        self.name = name
        self.roll_no = roll_no
        self.marks = float(marks)
    def _calculate_grade(self) -> str:
        """Return the grade for the student's marks.
        Bands (inclusive):
        90-100 -> A+
        75-89  -> A
        60-74  -> B
        50-59  -> C
        0-49   -> F (Fail)
        """
        percent = self.marks
        if percent < 0:
            percent = 0
        elif percent > 100:
            percent = 100
        for grade_label, (min_p, max_p) in self.GRADE_BANDS.items():
            if min_p <= percent <= max_p:
                return grade_label
        return "F (Fail)"
    def display_details(self) -> None:
        """Display student's name, roll number, marks, and grade."""
        grade = self._calculate_grade()
        print(f"Name   : {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks  : {self.marks}")
        print(f"Grade  : {grade}")
if __name__ == "__main__":
    print("Student Class and Display Details")
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                break
            print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid number for marks.")
    student = Student(name=name, roll_no=roll_no, marks=marks)
    student.display_details()