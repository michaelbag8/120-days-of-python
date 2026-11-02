def generate_movie_id(movies):
    if not movies:
        return f"M001"
    
    numbers = [int(movie.get("id").lstrip("M")) for movie in movies]
  
    highest_number = max(numbers)
    next_number = highest_number + 1

    return f"M{next_number:03d}"


def add_movie(movies, title, year, rating, watched):
    new_id = generate_movie_id(movies)
    for movie in movies:
        if new_id == movie.get("id"):
            raise ValueError(f"Sorry {new_id} already exist")
    new_movies = {
            "id": new_id,
            "title": title,
            "year": year,
            "rating": rating,
            "watched": watched
        }
    movies.append(new_movies)
    return new_movies
 
def list_movies(movies):
    if not movies:
        return "Sorry, no movies have been added yet"
    return movies


def show_menu():
    print("=====Movies Catalogue=====")
    print("1. Add Movie")
    print("2. View Movie")
    print("3. Find Movie By ID")
    print("4. Exit")

movies = []
while True:
    show_menu()
    choice = input("Select an option: ")
    if choice == "4":
        print("Goodbye!")
        break

    if choice == "1":
        title= input("Enter movie title: ").strip()
        year=int(input("Enter the year: "))
        rating=float(input("Enter the rating: "))
        watched=input("Have you watched the movie (True or False): ")
        try:
            add_movie(movies, title, year, rating, watched)
            print("Successfully added....")
        except ValueError as e:
            print(e)
    elif choice == "2":
        print(list_movies(movies))
    elif choice == "3":
        id_ = input("Enter movie id to search: ")
        movie = find_movie_by_id(movies,id_)
        print(movie)
    else:
        print(f"Sorry {choice} is invalid")
        continue


def find_movie_by_id(movies, movie_id):
    for movie in movies:
        if movie.get("id") == movie_id:
            return movie
    return None
