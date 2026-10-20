import requests

GREEN = "\033[1;32m"
RED = "\033[91m"
BLUE    = "\033[1;34m"
YELLOW  = "\033[1;33m"
RESET = "\033[0m"

def weather_report(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=1a8863cfe7c34bf48fe113421262010&q={city}"
    response = requests.get(url)
    data = response.json()

    temperature = data.get("current").get("temp_c")
    description = data.get("current").get("condition").get("text")
    report = f"{GREEN}Today's weather in {city} is, {description} and {temperature} degrees{RESET}"

    return report

def report(json):
    print(f"{YELLOW}The Current People In Space Are: {RESET}")

    for i, person in enumerate(json["people"], start=1):
        print(f"{i}. {person['name']}")


def people_on_space():
    url = "http://api.open-notify.org/astros.json"

    people = requests.get(url)

    json = people.json()
    reports = report(json)

    return reports


def currency_exchange():
    try:
        from_code = input("\nFrom currency code (e.g. USD): ").upper()

        url = f"https://open.er-api.com/v6/latest/{from_code}"

        response = requests.get(url)
        data = response.json()

        if data.get("result") == "error":

            raise KeyError("Invalid base currency code.")

        to_code = input("Enter the target currency code (e.g. INR, EUR, JPY): ").upper()

        if to_code not in data["rates"]:
            raise KeyError("Invalid target currency code.")

        rate = data["rates"][to_code]
        amount = float(input("Enter amount: "))

        converted = rate * amount
        print(f"{GREEN}\n {amount:,.2f} {from_code} = {converted:,.2f} {to_code}{RESET}")

    except ValueError:
        print("Error: Please enter a valid number for the amount.")

    except KeyError as e:
        print(f"Error: {e if str(e) else 'Invalid currency code.'} Please try again.")

    except requests.exceptions.RequestException as e:
        print(f"Network Error: Could not connect to the API. ({e})")

    except Exception as e:
        print(f"Something went wrong: {e}")


def display_menu():
    print(f"{GREEN}\n==== Welcome To My Garbage Of 3 In One Projects ===={RESET}")
    print("1. Weather Report")
    print("2. List of People Currently In Space")
    print("3. Currency Exchange")
    print("4. Quit")
  
while True:
    display_menu()
    choice = input(f"{BLUE}Select an option: {RESET}").strip()

    if choice == "4":
        print("Goodbye!")
        break

    if choice == "1":
        city = input("Please enter a city of your choice to get weather report: ").strip().title()
        print(weather_report(city))

    elif choice == "2":
        people_on_space()

    elif choice == "3":
        currency_exchange()

    else:
        print(f"{RED}Sorry '{choice}' an incorrect option (Options: 1, 2, 3 and 4){RESET}")




