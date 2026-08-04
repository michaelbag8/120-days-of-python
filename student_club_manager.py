student = ("Terkimbi Tergu", 56, "Geology")


def student_info(item):
    name, age, department = item
    return f"Name: {name}\nAge: {age}\nDepartment: {department}"


def show_menu():
    print("==== Student Club Manager ====")
    print("1. Add Member")
    print("2. Remove Member")
    print("3. View Members")
    print("4. Check Membership")
    print("5. Count Members")
    print("6. Show Unique Members")
    print("7. Exit")


def add_member(members):
    name = input("Enter member name: ").strip()
    if name in members:
        print(f"{name} already exists")
    else:
        members.add(name)
        print(f"{name} added successfully")
    return members


def remove_member(members):
    name = input("Enter member name: ").strip()
    if name in members:
        members.discard(name)
        print("Member removed")
    else:
        print("Member not found")
    return members


def view_members(members):
    print("Current Members")
    if len(members) == 0:
        print("No members yet")
    else:
        for name in members:
            print(name)


def check_membership(members):
    name = input("Enter member: ").strip()
    if name in members:
        print(f"{name} is a member")
    else:
        print(f"{name} is not a member")


def count_members(members):
    print("Total members:", len(members))


def show_unique_members(members):
    print("Unique Members")
    print("(Sets automatically remove duplicates, so every name below is unique)")
    for name in members:
        print(name)


def main():
    print("==== Student Information ====")
    print(student_info(student))

    members = set()

    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            members = add_member(members)
        elif choice == "2":
            members = remove_member(members)
        elif choice == "3":
            view_members(members)
        elif choice == "4":
            check_membership(members)
        elif choice == "5":
            count_members(members)
        elif choice == "6":
            show_unique_members(members)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print(f"{choice} is an unknown option")


if __name__ == "__main__":
    main()
