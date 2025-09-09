students = {}

def insert_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    students[student_id] = name
    print(f"Student {name} with ID {student_id} inserted.")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print(f"Student with ID {student_id} deleted.")
    else:
        print("Student ID not found.")

def search_student():
    student_id = input("Enter student ID to search: ")
    if student_id in students:
        print(f"Student found: ID={student_id}, Name={students[student_id]}")
    else:
        print("Student ID not found.")

def display_students():
    if students:
        print("All students:")
        for sid, name in students.items():
            print(f"ID: {sid}, Name: {name}")
    else:
        print("No students in the dictionary.")

while True:
    print("\nOptions: 1)insert | 2)delete | 3)search | 4)display | 5)exit")
    choice = input("Enter your choice: ").lower()
    
    if choice == '1':
        insert_student()
    elif choice == '2':
        delete_student()
    elif choice == '3':
        search_student()
    elif choice == '4':
        display_students()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid option, try again.")
