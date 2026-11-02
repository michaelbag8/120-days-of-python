def generate_movie_id(movies):
    if not movies:
        return f"M001"
    
    numbers = [int(movie.get("id").lstrip("M")) for movie in movies]
  
    highest_number = max(numbers)
    next_number = highest_number + 1

    return f"M{next_number:03d}"
