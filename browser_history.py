class BrowserHistory:
    def __init__(self):
        self.history = []

    @staticmethod
    def show_menu():
        print("==== Browser History ====")
        print("1. Visit website")
        print("2. Go back")
        print("3. View current page")
        print("4. View history")
        print("5. Exit")

    def add(self, website):
        self.history.append(website)
        return self.history

    def view_history(self):
        print("\nHistory")
        if not self.history:
            print("No visited sites yet.")
            return

        for index, site in enumerate(self.history, start=1):
            print(f"{index}: {site}")

    def go_back(self):
        if not self.history:
            print("No previous page to go back to.")
            return None

        return self.history.pop()

    def current_page(self):
        if not self.history:
            print("\nCurrent Page")
            print("No current page available.")
            return None

        print("\nCurrent Page")
        return self.history[-1]


def main():
    browser_history = BrowserHistory()

    while True:
        browser_history.show_menu()
        choice = input("Make your choice: ").strip()

        if choice == "5":
            print("Goodbye")
            break

        if choice == "1":
            site = input("Enter the site to visit: ").strip()
            if site:
                browser_history.add(site)
            else:
                print("Please enter a valid site.")

        elif choice == "2":
            previous = browser_history.go_back()
            if previous is not None:
                print(previous)

        elif choice == "3":
            page = browser_history.current_page()
            if page is not None:
                print(page)

        elif choice == "4":
            browser_history.view_history()

        else:
            print(f"Sorry {choice} is not a valid choice")


if __name__ == "__main__":
    main()

