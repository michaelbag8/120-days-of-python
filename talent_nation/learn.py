
resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []



def check_for_positive_int(text):
    text = str(text).strip()
    if text.isdigit() and int(text) > 0:
        return True
    return False


def find_resource(resource_id):
    resource_id = str(resource_id).strip().upper()
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    return None


def units_on_loan(fellow_id, resource_id):
    count = 0
    for record in borrow_records:
        if record["fellow_id"] == fellow_id and record["resource_id"] == resource_id:
            count = count + record["quantity"] - record["returned"]
    return count


def show_resource(resource):
    print(resource["id"], "|", resource["name"], "|", resource["category"],
          "| total:", resource["total"], "| available:", resource["available"])



def add_resource(resource_id, name, category, total):
    resource_id = str(resource_id).strip().upper()
    name = str(name).strip()
    category = str(category).strip()

    if resource_id == "" or name == "" or category == "":
        print("ID, name and category cannot be empty.")
        return False
    if find_resource(resource_id) is not None:
        print("A resource with ID", resource_id, "already exists.")
        return False
    if not check_for_positive_int(total):
        print("Total units must be a positive whole number.")
        return False

    total = int(total)
    new_resource = {"id": resource_id, "name": name, "category": category,
                    "total": total, "available": total}
    resources.append(new_resource)
    print("Added", name, "with", total, "units.")
    return True


def list_resources():
    if len(resources) == 0:
        print("No resources yet.")
    for resource in resources:
        show_resource(resource)



def borrow_resource(fellow_id, resource_id, quantity):
    fellow_id = str(fellow_id).strip().upper()

    if fellow_id not in fellows:
        print("unknown fellow ID", fellow_id)
        return False

    resource = find_resource(resource_id)
    if resource is None:
        print("unknown resource ID", str(resource_id).strip().upper())
        return False

    if not check_for_positive_int(quantity):
        print("quantity must be a positive whole number.")
        return False

    quantity = int(quantity)
    if quantity > resource["available"]:
        print("not enough stock. Requested", quantity,
              "but only", resource["available"], "available.")
        return False

    resource["available"] = resource["available"] - quantity
    record = {"fellow_id": fellow_id, "resource_id": resource["id"],
              "quantity": quantity, "returned": 0}
    borrow_records.append(record)
    print(fellows[fellow_id], "borrowed", quantity, resource["name"] + "(s).",
          "Available now:", resource["available"])
    return True



def return_resource(fellow_id, resource_id, quantity):
    fellow_id = str(fellow_id).strip().upper()

    if fellow_id not in fellows:
        print("unknown fellow ID", fellow_id)
        return False

    resource = find_resource(resource_id)
    if resource is None:
        print("unknown resource ID", str(resource_id).strip().upper())
        return False

    if not check_for_positive_int(quantity):
        print("quantity must be a positive whole number.")
        return False

    quantity = int(quantity)
    has = units_on_loan(fellow_id, resource["id"])
    if quantity > has:
        print(fellows[fellow_id], "only has", has, resource["name"] + "(s)",
              "on loan, so cannot return", quantity)
        return False

    
    still_to_return = quantity
    for record in borrow_records:
        if still_to_return == 0:
            break
        if record["fellow_id"] == fellow_id and record["resource_id"] == resource["id"]:
            not_yet_returned = record["quantity"] - record["returned"]
            if not_yet_returned > still_to_return:
                amount = still_to_return
            else:
                amount = not_yet_returned
            record["returned"] = record["returned"] + amount
            still_to_return = still_to_return - amount

   
    resource["available"] = resource["available"] + quantity
    print(fellows[fellow_id], "returned", quantity, resource["name"] + "(s).",
          "Available now:", resource["available"])
    return True


def search_by_name(search_text):
    search_text = search_text.strip().lower()
    matches = []
    if search_text == "":
        return matches
    for resource in resources:
        if search_text in resource["name"].lower():
            matches.append(resource)
    return matches


def filter_by_category(category):
    category = category.strip().lower()
    matches = []
    for resource in resources:
        if resource["category"].lower() == category:
            matches.append(resource)
    return matches


def show_matches(matches):
    if len(matches) == 0:
        print("No matching resources found.")
    for resource in matches:
        show_resource(resource)



def show_report():
    total_units = 0
    available_units = 0
    borrowed_units = 0
    most_borrowed = 0

    loans = {}
    for resource in resources:
        total_units = total_units + resource["total"]
        available_units = available_units + resource["available"]
        loans[resource["id"]] = 0
    for record in borrow_records:
        loans[record["resource_id"]] += record["quantity"] - record["returned"]

    for resource_id in loans:
        borrowed_units = borrowed_units + loans[resource_id]
        if loans[resource_id] > most_borrowed:
            most_borrowed = loans[resource_id]

    print("Total units:", total_units)
    print("Available units:", available_units)
    print("Borrowed units:", borrowed_units)

    print("Resources with fewer than 3 available units:")
    found_low = False
    for resource in resources:
        if resource["available"] < 3:
            print("  -", resource["name"], "(" + str(resource["available"]) + ")")
            found_low = True
    if not found_low:
        print("  None")

 
    if most_borrowed == 0:
        print("Most borrowed resource: none (nothing is on loan)")
    else:
        print("Most borrowed resource (" + str(most_borrowed) + " units on loan):")
        for resource in resources:
            if loans[resource["id"]] == most_borrowed:
                print("  -", resource["name"])



def show_menu():
    print("\n===== Learn2Earn Equipment Lending =====")
    print("1. Add resource")
    print("2. List resources")
    print("3. Borrow")
    print("4. Return")
    print("5. Search by name")
    print("6. Filter by category")
    print("7. Report")
    print("0. Exit")


def main():
    running = True
    while running:
        show_menu()
        try:
            choice = input("Choose an option: ").strip()

            if choice == "1":
                resource_id = input("Resource ID: ")
                name = input("Name: ")
                category = input("Category: ")
                total = input("Total units: ")
                add_resource(resource_id, name, category, total)
            elif choice == "2":
                list_resources()
            elif choice == "3":
                print("Fellows:", fellows)
                fellow_id = input("Fellow ID: ")
                resource_id = input("Resource ID: ")
                quantity = input("Quantity: ")
                borrow_resource(fellow_id, resource_id, quantity)
            elif choice == "4":
                print("Fellows:", fellows)
                fellow_id = input("Fellow ID: ")
                resource_id = input("Resource ID: ")
                quantity = input("Quantity: ")
                return_resource(fellow_id, resource_id, quantity)
            elif choice == "5":
                show_matches(search_by_name(input("Name to search: ")))
            elif choice == "6":
                show_matches(filter_by_category(input("Category: ")))
            elif choice == "7":
                show_report()
            elif choice == "0":
                print("Goodbye!")
                running = False
            else:
                print("Invalid choice. Please enter a number from 0 to 7.")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            running = False

main()