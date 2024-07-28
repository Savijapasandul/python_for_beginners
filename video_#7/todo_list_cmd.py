todos = []

def display_todos(todos):
    if not todos:
        print("No taska in the to-do list.")
    else: 
        for idx, todo in enumerate(todos, 1):
            print(f"{idx}, {todo}")

def add_todo():
    todo = input("Enter a new to-do: ")
    todos.append(todo)
    print("To-do added")

def delete_todo():
    display_todos(todos)
    idx = int(input("Enter the number of the to-do to delete: "))
    if 0 < idx <= len(todos):
        todos.pop(idx-1)
        print("To-do deleted.")
    else:
        print("Invalid number.")

while True: 
    print("\n1. Display to-dos\n2. Add to-do\n3. Delete to-do\n4. Quit")
    choice = input("Enter your choice.")
    if choice == '1':
        display_todos(todos)
    elif choice == '2':
        add_todo()
    elif choice == '3':
        delete_todo()
    elif choice == '4':
        break 
    else: 
        print("Invalid choice. Please try again.")

    