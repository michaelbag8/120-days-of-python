from football_analyzer import calculate_team_goals

def test_teams_goals_normal_input():
    teams = [
    {"id": "P001", "name": "Salah", "team": "Liverpool", "goals": 18, "matches": 12},
    {"id": "P002", "name": "Diaz", "team": "Liverpool", "goals": 12, "matches": 10},
    {"id": "P003", "name": "Haaland", "team": "Man City", "goals": 22, "matches": 12},
    {"id": "P004", "name": "Foden", "team": "Man City", "goals": 15, "matches": 11},
    {"id": "P005", "name": "Saka", "team": "Arsenal", "goals": 16, "matches": 12},
    {"id": "P006", "name": "Odegaard", "team": "Arsenal", "goals": 10, "matches": 10},
    {"id": "P007", "name": "Palmer", "team": "Chelsea", "goals": 14, "matches": 12}
]

    result = calculate_team_goals(teams)
    assert result == {'Liverpool': 30, 'Man City': 37, 'Arsenal': 26, 'Chelsea': 14}

def test_teams_goals_empty_input():
    assert calculate_team_goals([]) == {}
   
def test_teams_goals_single_player_input():
    team = [
        {"id": "P001", "name": "Palmer", "team": "Chelsea", "goals": 14, "matches": 12}
    ]
    result = calculate_team_goals(team)
    assert result == {'Chelsea': 14}

def test_teams_goals_multiple_players_input():
    teams = [
        {"id": "P001", "name": "Salah", "team": "Liverpool", "goals": 18, "matches": 12},
        {"id": "P002", "name": "Diaz", "team": "Liverpool", "goals": 12, "matches": 10},
    ]
    result = calculate_team_goals(teams)
    assert result == {'Liverpool': 30}