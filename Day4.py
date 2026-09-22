class Grade:
    s1 = "Python"
    s2 = "DBMS"
    s3 = "Operating System"
    s4 = "Computer Networks"
    s5 = "DAA"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def addMarks(self):
        self.marks[self.s1] = int(input("Enter Python marks: "))
        self.marks[self.s2] = int(input("Enter DBMS marks: "))
        self.marks[self.s3] = int(input("Enter OS marks: "))
        self.marks[self.s4] = int(input("Enter CN marks: "))
        self.marks[self.s5] = int(input("Enter DAA marks: "))

    def viewMarks(self):
        print("\nStudent Name:", self.name)

        for subject, marks in self.marks.items():
            print(subject, ":", marks)

    def totalMarks(self):
        total = sum(self.marks.values())
        print("Total Marks:", total)

    def percentage(self):
        total = sum(self.marks.values())
        percentage = total / 5
        print("Percentage:", percentage, "%")

    def calculateGrade(self):
        percentage = sum(self.marks.values()) / 5

        if percentage >= 90:
            print("Grade: A+")
        elif percentage >= 80:
            print("Grade: A")
        elif percentage >= 70:
            print("Grade: B")
        elif percentage >= 60:
            print("Grade: C")
        elif percentage >= 50:
            print("Grade: D")
        else:
            print("Grade: F")


name = input("Enter Student Name: ")

student = Grade(name, {})

while True:
    print("\n===== COLLEGE GRADING SYSTEM =====")
    print("1. Add Marks")
    print("2. View Marks")
    print("3. Total Marks")
    print("4. Percentage")
    print("5. Calculate Grade")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student.addMarks()

    elif choice == 2:
        student.viewMarks()

    elif choice == 3:
        student.totalMarks()

    elif choice == 4:
        student.percentage()

    elif choice == 5:
        student.calculateGrade()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")