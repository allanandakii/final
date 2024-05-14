gradebook = {}
math_gradebook = {}
science_gradebook = {}
history_gradebook = {}
print("Welcome to the Student Gradebook!")
print("1. Add a new student and their grades")
print("2. View a student's grades")
print("3. View the average grade for a student")
print("4. View the average grade for a specific subject")
print("5. Exit")

choice = int(input("Please enter your choice: "))
if choice == 1:
    name = input("Enter your name: ")
    math_grade = int(input("Enter Math grade: "))
    science_grade = int(input("Enter Science grade: "))
    history_grade = int(input("Enter History grade: "))
    gradebook[name] = [math_grade, science_grade, history_grade]
    print("Student " + name + " has been added to the gradebook.")
    print("")
    choice = int(input("Please enter your choice: "))
if choice == 2:
    name = input("Enter your name: ")
    if name in gradebook:
        print("Grades for " + name + ": ")
        print("Math: " + str(gradebook[name][0]))
        print("Science: " + str(gradebook[name][1]))
        print("History: " + str(gradebook[name][2]))
        print("")
        choice = int(input("Please enter your choice: "))
    elif name not in gradebook:
        print("Name is not in gradebook.")
        print("")
        choice = int(input("Please enter your choice: "))
if choice == 3:
    name = input("Enter your name: ")
    total = gradebook[name][0] + gradebook[name][1] + gradebook[name][2]
    average = total/3
    print("Average grade for " + name + ": " + str(average))
    print("")
    choice = int(input("Please enter your choice: "))
if choice == 4:
    print("Math = 1")
    print("Science = 2")
    print("History = 3")
    subject = int(input("Select which subject you would like to calculate: "))
    if subject == 1:
        num = 1
        total_math = 0
        for i in range(3):
            math_grades = int(input("Please enter grade " + str(num) + ": "))
            total_math = total_math + math_grades
            num = num + 1
        print("Math grade average: " + str(total_math/3))
        print("")
        choice = int(input("Please enter your choice: "))
    if subject == 2:
        num = 1
        total_science = 0
        for i in range(3):
            science_grades = int(input("Please enter grade " + str(num) + ": "))
            total_science = total_science + science_grades
            num = num + 1
        print("Science grade average: " + str(total_science/3))
        print("")
        choice = int(input("Please enter your choice: "))
    if subject == 3:
        num = 1
        total_history = 0
        print("You are going to enter 3 grades.")
        for i in range(3):
            history_grades = int(input("Please enter grade " + str(num) + ": "))
            total_history = total_history + history_grades
            num = num + 1
        print("History grade average: " + str(total_history/3))
        print("")
        choice = int(input("Please enter your choice: "))
if choice == 5:
    print("Bye-bye!")