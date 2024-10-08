# Initilize Dictionary
student_grade = { }

#Add a new student
def add_student(name,grade):
    student_grade[name] = grade
    # Rimsha] = 300
    print(f"Added {name} with a {grade}")
    # Added rimsha with a 300

#Update a student
def update_student(name,grade):
    if name in student_grade:
        # rimsha = 200
        print(f"{name} with marks are updated {grade}")

    else:
        print(f"{name} is not found")

# Delete a student
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been successfully deleted")

    else:
        print(f"{name} is not found") 

# view all students
def display_all_students():
    if student_grade:
        for name,grade in student_grade.items():
            print(f"{name} : {grade}")

    else:
        print("No student found/added")

# display_all_students() 
# Main function to run the program

def main():
    while True:
        print('\n Student Grade Management System')
        print("1.Add Student")
        print("2.Update Student")
        print("3.Delete Student")
        print("4. View Student")
        print("5.Exit")

        choice = int (input("Enter your choice = "))                                   
        if choice == 1:
            name = input("Enter student name  = ")
            grade = int(input("Enter student grade = "))
            add_student(name,grade)

        elif choice == 2:
            name = input("Enter student name you want to update = ")
            grade = int (input("Enter student grade = "))
            update_student(name,grade)

        elif choice == 3:
            name =  input("Enter name of student you want to deleted = ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program...")

        else:
            print("Invalid Choice")          
# Run the main function
if __name__ == "__main__":
    main()