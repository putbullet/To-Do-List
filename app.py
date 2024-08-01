user_input = 'random'
tasks = []

def show_menu():
    """Displays the menu options to the user."""
    print("\n"
          "███╗   ███╗███████╗███╗   ██╗██╗   ██╗\n"
          "████╗ ████║██╔════╝████╗  ██║██║   ██║\n"
          "██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║\n"
          "██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║\n"
          "██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝\n"
          "╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝\n")
    print("1. Add an item")
    print("2. Mark as done")
    print("3. View items")
    print("4. Exit")

while user_input != '4':
    show_menu()
    user_input = input("Enter your choice: ").strip()

    if user_input == '1':
        task = input("What's to be done? ").strip()
        if task:
            tasks.append(task)
            print(f"Added item: {task}")
        else:
            print("Cannot add an empty task.")
    elif user_input == '2':
        if not tasks:
            print("No items to mark as done.")
        else:
            task_to_remove = input("Enter the task to mark as done: ").strip()
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
                print(f"Removed item: {task_to_remove}")
            else:
                print("Item does not exist in the list.")
    elif user_input == '3':
        if not tasks:
            print("No items in the to-do list.")
        else:
            print("List of to-do items:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
    elif user_input == '4':
        print("Goodbye!")
    else:
        print("Please enter a valid choice.")
