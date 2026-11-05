from football_analyzer import calculate_team_goals, calculate_average_goals_per_team, find_highest_scoring_team, filter_teams_by_goals, rank_teams

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


def test_normal_team_average():
    players = [
    {"id": "P001", "name": "Salah", "team": "Liverpool", "goals": 18, "matches": 12},
    {"id": "P002", "name": "Diaz", "team": "Liverpool", "goals": 12, "matches": 10},
    {"id": "P003", "name": "Haaland", "team": "Man City", "goals": 22, "matches": 12},
    {"id": "P004", "name": "Foden", "team": "Man City", "goals": 15, "matches": 11},
    {"id": "P005", "name": "Saka", "team": "Arsenal", "goals": 16, "matches": 12},
    {"id": "P006", "name": "Odegaard", "team": "Arsenal", "goals": 10, "matches": 10},
    {"id": "P007", "name": "Palmer", "team": "Chelsea", "goals": 14, "matches": 12}
]
    result = calculate_average_goals_per_team(players)
    assert result == {'Liverpool': 15.0, 'Man City': 18.5, 'Arsenal': 13.0, 'Chelsea': 14.0}

def test_empty_team_average():
    assert calculate_average_goals_per_team([]) == {}
    

def test_single_team_average():
    players =[
        {"id": "P001", "name": "Salah", "team": "Liverpool", "goals": 18, "matches": 12}
    ]
    result = calculate_average_goals_per_team(players)
    assert result == {"Liverpool": 18.0}

def test_multiple_team_average():
    players = [
        {"id": "P001", "name": "Salah", "team": "Liverpool", "goals": 18, "matches": 12},
        {"id": "P002", "name": "Diaz", "team": "Liverpool", "goals": 12, "matches": 10},
    ]
    result = calculate_average_goals_per_team(players)
    assert result == {'Liverpool': 15.0}

def test_normal_team_scores_input():
    players = [
    {"name": "Salah", "team": "Liverpool", "goals": 18},
    {"name": "Diaz", "team": "Liverpool", "goals": 12},
    {"name": "Haaland", "team": "Man City", "goals": 22},
    {"name": "Foden", "team": "Man City", "goals": 15},
    {"name": "Saka", "team": "Arsenal", "goals": 16},
    {"name": "Odegaard", "team": "Arsenal", "goals": 10},
    {"name": "Palmer", "team": "Chelsea", "goals": 14},
]
    result = find_highest_scoring_team(players)
    assert result == ('Man City', 37)

def test_empty_team_scores_input():
    assert find_highest_scoring_team([]) is None

def test_tie_team_scores_input():
    players = [
    {"name": "Salah", "team": "Liverpool", "goals": 22},
    {"name": "Diaz", "team": "Liverpool", "goals": 15},
    {"name": "Haaland", "team": "Man City", "goals": 22},
    {"name": "Foden", "team": "Man City", "goals": 15},
    {"name": "Saka", "team": "Arsenal", "goals": 16},
    {"name": "Odegaard", "team": "Arsenal", "goals": 10},
    {"name": "Palmer", "team": "Chelsea", "goals": 14},
]
    result = find_highest_scoring_team(players)
    assert result == ('Liverpool', 37)

def test_one_team_highest_score_input():
    players = [
    {"name": "Salah", "team": "Liverpool", "goals": 18},
    {"name": "Diaz", "team": "Liverpool", "goals": 12},
    {"name": "Haaland", "team": "Man City", "goals": 22},
    {"name": "Foden", "team": "Man City", "goals": 15},
    {"name": "Saka", "team": "Arsenal", "goals": 16},
    {"name": "Odegaard", "team": "Arsenal", "goals": 10},
    {"name": "Palmer", "team": "Chelsea", "goals": 14},
]
    result = find_highest_scoring_team(players)
    assert result == ('Man City', 37)


def test_normal_filter_with_minimum():
    players = [
    {"name": "Salah", "team": "Liverpool", "goals": 18},
    {"name": "Diaz", "team": "Liverpool", "goals": 12},
    {"name": "Haaland", "team": "Man City", "goals": 22},
    {"name": "Foden", "team": "Man City", "goals": 15},
    {"name": "Saka", "team": "Arsenal", "goals": 16},
    {"name": "Odegaard", "team": "Arsenal", "goals": 10},
    {"name": "Palmer", "team": "Chelsea", "goals": 14},
]
    result =filter_teams_by_goals(players, 25)
    assert result == {'Liverpool': 30, 'Man City': 37, 'Arsenal': 26}

def test_empty_input_with_minimum():
    assert filter_teams_by_goals([], 25) == {}
    
def test_no_team_meet_minimum():
    players = [
        {"name": "Salah", "team": "Liverpool", "goals": 18},
        {"name": "Pac", "team": "Aba Warriors", "goals": 12},
        {"name": "Haaland", "team": "Man City", "goals": 22},
    ]
    result =filter_teams_by_goals(players, 25)
    assert result == {}

def test_normal_filter_with_minimum():
    players = [
        {"name": "Salah", "team": "Liverpool", "goals": 18},
        {"name": "Pac", "team": "Aba Warriors", "goals": 25},
        {"name": "Haaland", "team": "Man City", "goals": 22},
    ]
    result =filter_teams_by_goals(players, 25)
    assert result == {"Aba Warriors": 25}


def test_normal_team_rank():
    players = [
    {"name": "Salah", "team": "Liverpool", "goals": 18},
    {"name": "Diaz", "team": "Liverpool", "goals": 12},
    {"name": "Haaland", "team": "Man City", "goals": 22},
    {"name": "Foden", "team": "Man City", "goals": 15},
    {"name": "Saka", "team": "Arsenal", "goals": 16},
    {"name": "Odegaard", "team": "Arsenal", "goals": 10},
    {"name": "Palmer", "team": "Chelsea", "goals": 14},
]
    result = rank_teams(players)
    assert result == [('Man City', 37), ('Liverpool', 30), ('Arsenal', 26), ('Chelsea', 14)]

def test_empty_team_rank():
    assert rank_teams([]) == []
    
def test_one_team_rank():
    players = [
        {"name": "Palmer", "team": "Chelsea", "goals": 14},
    ]
    result = rank_teams(players)
    assert result == [("Chelsea", 14)]

def test_tie_team_rank():
    players = [
    {"name": "Odegaard", "team": "Arsenal", "goals": 10},
    {"name": "Palmer", "team": "Chelsea", "goals": 10},
]
    result = rank_teams(players)
    assert result == [("Arsenal", 10), ("Chelsea", 10)]