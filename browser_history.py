def show_menu():
    print("==== Browser History ====")
    print("1. Visit website")
    print("2. Go back")
    print("3. View current page")
    print("4. View history")
    print("5. Exit")

history = []

def add(website):
    history.append(website)
    return history

def view_history():
    print("\nHistory")
    for index, items in enumerate(history, start=1):
        print(f"{index}: {items}")

def go_back():
    back = history.pop()
    return back

def current_page():
    print("\nCurrent Page")
    current = history[-1]
    return current

while True:
    show_menu()
    choice = input("Make your choice: ")

    if choice == "5":
        print("Goodbye")
        break

    if choice == "1":
        site = input("Enter the site to visit: ").strip()
        add(site)

    elif choice == "2":
        print(go_back())

    elif choice == "3":
        print(current_page())

    elif choice == "4":
        view_history()

    else:
        print(f"Sorry {choice} is not a valid choice")
    




