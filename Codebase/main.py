# Student Fee Management System

# Course fee dictionary
course_fees = {
    "BCA": 45000,
    "BTech": 60000,
    "MBA": 80000
}

# List to store student dictionaries
students = []


# Find student using roll number
def find_student(roll):
    for student in students:
        if student["roll"] == roll:
            return student
    return None


# Show student details
def show_student(student):
    due = student["total"] - student["paid"]

    if due == 0:
        status = "Paid"
    elif student["paid"] == 0:
        status = "Unpaid"
    else:
        status = "Partial"

    print("\nRoll:", student["roll"])
    print("Name:", student["name"])
    print("Course:", student["course"])
    print("Total Fee:", student["total"])
    print("Paid:", student["paid"])
    print("Due:", due)
    print("Status:", status)


# Add student
def add_student():
    roll = input("Enter Roll Number: ")

    if find_student(roll) != None:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    course = input("Enter Course (BCA/BTech/MBA): ").upper()

    if course not in course_fees:
        print("Invalid Course!")
        return

    student = {
        "roll": roll,
        "name": name,
        "course": course,
        "total": course_fees[course],
        "paid": 0
    }

    students.append(student)
    save_data()

    print("Student Added Successfully!")
    show_student(student)


# Pay student fee
def pay_fee():
    roll = input("Enter Roll Number: ")
    student = find_student(roll)

    if student == None:
        print("Student not found!")
        return

    amount = int(input("Enter Amount: "))

    due = student["total"] - student["paid"]

    if amount <= 0:
        print("Invalid payment amount!")

    elif amount > due:
        print("Amount exceeds due. Payment rejected.")

    else:
        student["paid"] += amount
        save_data()

        print("Payment Received Successfully!")
        show_student(student)


# Search student
def search_student():
    roll = input("Enter Roll Number: ")
    student = find_student(roll)

    if student != None:
        show_student(student)
    else:
        print("Student not found!")


# Show pending dues
def pending_dues():
    print("\nStudents Having Pending Dues:")

    found = False

    for student in students:
        due = student["total"] - student["paid"]

        if due > 0:
            print(student["roll"], student["name"], "Due:", due)
            found = True

    if found == False:
        print("No Pending Dues!")


# Save records in file
def save_data():
    file = open("fees.txt", "w")

    for student in students:
        line = (
            student["roll"] + "|" +
            student["name"] + "|" +
            student["course"] + "|" +
            str(student["total"]) + "|" +
            str(student["paid"]) + "\n"
        )

        file.write(line)

    file.close()


# Load records from file
def load_data():
    try:
        file = open("fees.txt", "r")

        for line in file:
            data = line.strip().split("|")

            student = {
                "roll": data[0],
                "name": data[1],
                "course": data[2],
                "total": int(data[3]),
                "paid": int(data[4])
            }

            students.append(student)

        file.close()

    except FileNotFoundError:
        pass


# Main program
load_data()

while True:

    print("\n===== STUDENT FEE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Pay Fee")
    print("3. Search Student")
    print("4. Pending Dues")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        pay_fee()

    elif choice == "3":
        search_student()

    elif choice == "4":
        pending_dues()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
