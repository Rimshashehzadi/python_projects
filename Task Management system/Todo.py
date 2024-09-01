def task():
    tasks = [] #empty
    print("----------WELCOME TO THE MANAGEMENT APP----------")

    total_task = int (input("Enter hoe many task you want to add = "))
    for i in range(1,total_task):
        task_name = input(f"Enter task {i} = ") # enter task
        tasks.append(task_name)

    print("Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        if operation == 1:
            add = input("Enter the task name you want to add =")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            update_val = input("Enter the task name you want to update = ")
            if update_val in tasks:
               up = input("Enter new task = ")
               ind = tasks.index(update_val)
               tasks[ind] = up
               print(f"Update task {up}")
    