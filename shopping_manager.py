# to be refactor later
def show_menu():
    print("\n==== Shopping List Manager ====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Items")
    print("4. Count Items")
    print("5. Exit")


shopping_list = []

while True:
    show_menu()

    choice = input("Choose an option: ").strip()

    if choice == "1":
        item = input("Enter an item to add: ").strip()

        if item == "":
            print("Item cannot be empty.")
        else:
            shopping_list.append(item)
            print(f'"{item}" added successfully.')

    elif choice == "2":
        item = input("Enter an item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(f'"{item}" removed successfully.')
        else:
            print(f'"{item}" does not exist in the shopping list.')

    elif choice == "3":
        if len(shopping_list) == 0:
            print("Shopping list is empty.")
        else:
            print("\nShopping List")
            for i in range(len(shopping_list)):
                print(f"{i + 1}. {shopping_list[i]}")

    elif choice == "4":
        print(f"Total items: {len(shopping_list)}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number between 1 and 5.")
