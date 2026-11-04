def calculate_points(team):
    return (team["won"] * 3) + team["drawn"]

def calculate_goal_difference(team):
    return team["goals_for"] - team["goals_against"]


def get_ranking(team):
    points = calculate_points(team)
    goals_diff = calculate_goal_difference(team)
    goals = team["goals_for"]
    return (points, goals_diff, goals)

def sort_teams(teams):
    return sorted(teams, key=get_ranking, reverse=True)

teams = [
    {"play": "Arsenal", "played": 30, "won": 22, "drawn": 5, "lost": 3, "goals_for": 65, "goals_against": 25},
    {"play": "Liverpool", "played": 30, "won": 21, "drawn": 7, "lost": 2, "goals_for": 68, "goals_against": 28},
    {"play": "Chelsea", "played": 30, "won": 18, "drawn": 6, "lost": 6, "goals_for": 55, "goals_against": 30},
    {"play": "Man City", "played": 30, "won": 22, "drawn": 5, "lost": 3, "goals_for": 70, "goals_against": 25}
]


# result = sort_teams(teams)
# for index, team in enumerate(result, start=1):
#     points = calculate_points(team)
#     print(f"{index}. {team['play']} - {points} points")

# Data Transformation

def build_players_by_id(players):
    return {
        player["id"]: {
            "name": player["name"],
            "goals": player["goals"]
        }
        for player in players
        }
      

def calculate_total_goals(players):
    return sum(player["goals"] for player in players)
