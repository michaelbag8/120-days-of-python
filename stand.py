def calculate_match_points(match, standings):
    home = match["home"]
    away = match["away"]

    home_goals = match["home_goals"]
    away_goals = match["away_goals"]

    if home == away:
        raise ValueError("A team cannot play against itself")
    

    standings.setdefault(home, 0)
    standings.setdefault(away, 0)
    
    
    if home_goals > away_goals:
        standings[home] += 3
    

    elif away_goals > home_goals:
        standings[away] += 3
   
    else:
        standings[home] += 1
        standings[away] += 1

    return standings


def calculate_league_standings(matches, original_standings):
    temporary_standing = {}

    for match in matches:
        calculate_match_points(match, temporary_standing)

    for team, points in temporary_standing.items():
        original_standings.setdefault(team, 0)
        original_standings[team] += points

    return original_standings

original_standings = {
    "Arsenal": 6,
    "Chelsea": 3
}

matches = [
    {"home": "Arsenal", "away": "Liverpool", "home_goals": 2, "away_goals": 0},
    {"home": "Chelsea", "away": "Liverpool", "home_goals": 1, "away_goals": 1}
]

print(calculate_league_standings(matches, original_standings))