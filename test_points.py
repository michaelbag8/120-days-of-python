from points import calculate_points, calculate_goal_difference, get_ranking

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
