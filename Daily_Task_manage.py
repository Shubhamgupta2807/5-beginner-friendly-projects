"""
📝 Daily Task Management App (Beginner Python Project)

This is a simple command-line Task Management application built using Python.
It allows users to:
- Add new tasks
- Update existing tasks
- Delete tasks
- View all tasks

The app runs in a loop until the user chooses to exit.
This project helps beginners practice core Python concepts like:
- Lists
- Functions
- Loops
- Conditional statements
- User input handling

A great beginner project to understand basic CRUD operations in Python.
"""

def task():
    tasks = []
    print("----Welcome to Task Management App----\n")

    total_task = int(input("Enter how many task u want too Add = "))
    for i in range(1 , total_task+1):
        task_name = input(f"Enter task {i} =")
        tasks.append(task_name)

    print(f"Today's tasks is - \n\t{tasks}.")

    while True:
        operation = int(input("Enter \n1- ADD\n2- UPDATE\n3- DELETE\n4- VIEW\n5- EXIT = "))
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"task {add} has been added successfully!")

        elif operation == 2:
            update_task = input("Enter task you want to update = ")
            if update_task in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(update_task)
                tasks[ind] = up
                print(f"Updated task {up}")

        elif operation == 3:
            delete_task = input("Enter task you want to delete = ")
            if delete_task in tasks:
                ind = tasks.index(delete_task)
                del tasks[ind]
                print(f"task {delete_task} has been deleted successfully")
            

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        
        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid input! plz input valid Number.")

task()