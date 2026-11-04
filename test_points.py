from points import calculate_points, calculate_goal_difference, get_ranking, sort_teams

def test_valid_calculation():
    result = calculate_points({
    "name": "Arsenal",
    "won": 22,
    "drawn": 5,
    "lost": 3,
    "played": 30,
    "goals_for": 65,
    "goals_against": 25
})
    assert result == 71

def test_valid_goal_difference():
    result = calculate_goal_difference({
    "name": "Arsenal",
    "won": 22,
    "drawn": 5,
    "lost": 3,
    "played": 30,
    "goals_for": 65,
    "goals_against": 25
})
    assert result == 40

def test_get_ranking():
    result = get_ranking({
    "name": "Arsenal", 
    "played": 30, 
    "won": 22, 
    "drawn": 5, 
    "lost": 3, 
    "goals_for": 65, 
    "goals_against": 25
})
    assert result == (71, 40, 65)

def test_teams_are_sorted_correctly():
    teams = [
    {"name": "Arsenal", "played": 30, "won": 22, "drawn": 5, "lost": 3, "goals_for": 65, "goals_against": 25},
    {"name": "Liverpool", "played": 30, "won": 21, "drawn": 7, "lost": 2, "goals_for": 68, "goals_against": 28},
    {"name": "Chelsea", "played": 30, "won": 18, "drawn": 6, "lost": 6, "goals_for": 55, "goals_against": 30},
    {"name": "Man City", "played": 30, "won": 22, "drawn": 5, "lost": 3, "goals_for": 70, "goals_against": 25}
]
    result = sort_teams(teams)
    assert [team["name"] for team in result] == ["Man City", "Arsenal", "Liverpool", "Chelsea"]

def test_stable_sorting():
    teams = [
    {"name": "Liverpool", "won": 20, "drawn": 10,
     "goals_for": 60, "goals_against": 35},

    {"name": "Man City", "won": 20, "drawn": 10,
     "goals_for": 60, "goals_against": 35}
]
    result = sort_teams(teams)
    assert [team['name'] for team in result] == ["Liverpool", "Man City"]
