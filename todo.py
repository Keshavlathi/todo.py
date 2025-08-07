def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def task():
    tasks = load_tasks()  
    print("---\nTodo List Manager\n---")

    while True:
        
        print(f"\n--- Current Tasks: {len(tasks)} ---")
        
        try:
            operation = int(input("\nChoose an operation:\n1-Add Tasks\n2-Update Tasks\n3-Delete Tasks\n4-View Tasks\n5-Exit/Stop/\n"))
            
            if operation == 1:
                total_tasks = int(input("How many tasks do you want to add = "))
                for i in range(total_tasks):
                    task_name = input(f"Enter task {i+1} = ")
                    tasks.append(task_name)
                print(f"Added {total_tasks} task(s) successfully!")

            elif operation == 2:
                updated_val = input("Enter the task name you want to update: ")
                if updated_val in tasks:
                    up = input(f"Enter the new task to replace '{updated_val}': ")
                    ind = tasks.index(updated_val)
                    tasks[ind] = up
                    print(f"Updated task to '{up}'")
                else:
                    print("Task not found!")

            elif operation == 3:
                del_value = input("Enter the task name you want to delete: ")
                if del_value in tasks:
                    ind = tasks.index(del_value)
                    del tasks[ind]
                    print(f"Task '{del_value}' successfully deleted...!")
                else:
                    print("Task not found!")

            elif operation == 4:
                print(f"Total tasks = {len(tasks)}")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
            
            elif operation == 5:
                save_tasks(tasks)
                print("Exiting Todo List Manager. Tasks saved. Goodbye!")
                break
            
            else:
                print("Invalid operation. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number from the menu.")
            
task()
