from matchups import generate_matchups, group_players_by_team, top_scoring_team, total_goals, top_scoring_teams


def test_empty_teams():
    result = generate_matchups([])
    assert result == []


def test_one_team():
    result = generate_matchups(["Arsenal"])
    assert result == []


def test_two_teams():
    result = generate_matchups(["Arsenal", "Chelsea"])
    assert result == ["Arsenal vs Chelsea"]


def test_four_teams():
    result = generate_matchups(["Arsenal", "Chelsea", "Liverpool", "Man City"])
    assert result == [
        "Arsenal vs Chelsea",
        "Arsenal vs Liverpool",
        "Arsenal vs Man City",
        "Chelsea vs Liverpool",
        "Chelsea vs Man City",
        "Liverpool vs Man City"
    ]

def test_group_players_by_team():
    players = [
    {"name": "Salah", "team": "Liverpool", "goals": 18},
    {"name": "Haaland", "team": "Man City", "goals": 22},
    {"name": "Saka", "team": "Arsenal", "goals": 16},
    {"name": "Messi", "team": "Inter Miami", "goals": 89}
]
    result = group_players_by_team(players)
    assert result == {
    "Liverpool": ["Salah"],
    "Man City": ["Haaland"],
    "Arsenal": ["Saka"],
    "Inter Miami": ["Messi"]
}

def test_empty_players():
    result = group_players_by_team([])
    assert result == {}

def test_players_from_same_team():
    players = [
    {"name": "Salah", "team": "Liverpool", "goals": 18},
    {"name": "Haaland", "team": "Man City", "goals": 22},
    {"name": "Saka", "team": "Arsenal", "goals": 16},
    {"name": "Diaz", "team": "Liverpool", "goals": 12}
]
    result = group_players_by_team(players)
    assert result == {
    "Liverpool": ["Salah", "Diaz"],
    "Man City": ["Haaland"],
    "Arsenal": ["Saka"]
}
    
def test_valid_input():
    players = [
    {"name": "Salah", "team": "Liverpool", "goals": 18},
    {"name": "Diaz", "team": "Liverpool", "goals": 12},
    {"name": "Haaland", "team": "Man City", "goals": 22},
    {"name": "Foden", "team": "Man City", "goals": 15},
    {"name": "Saka", "team": "Arsenal", "goals": 16},
    {"name": "Odegaard", "team": "Arsenal", "goals": 10},
    {"name": "Palmer", "team": "Chelsea", "goals": 14},
]
    result = top_scoring_team(players)
    assert result == ('Man City', 37)

def test_empty_input():
    assert top_scoring_team([]) is None

def test_tie_input():
    players = [
    {"name": "Salah", "team": "Liverpool", "goals": 22},
    {"name": "Diaz", "team": "Liverpool", "goals": 15},
    {"name": "Haaland", "team": "Man City", "goals": 22},
    {"name": "Foden", "team": "Man City", "goals": 15},
    {"name": "Saka", "team": "Arsenal", "goals": 16},
    {"name": "Odegaard", "team": "Arsenal", "goals": 10},
    {"name": "Palmer", "team": "Chelsea", "goals": 14},
]
    result = top_scoring_team(players)
    assert result == ('Liverpool', 37)

def test_one_team_highest_score():
    players = [
    {"name": "Salah", "team": "Liverpool", "goals": 18},
    {"name": "Diaz", "team": "Liverpool", "goals": 12},
    {"name": "Haaland", "team": "Man City", "goals": 22},
    {"name": "Foden", "team": "Man City", "goals": 15},
    {"name": "Saka", "team": "Arsenal", "goals": 16},
    {"name": "Odegaard", "team": "Arsenal", "goals": 10},
    {"name": "Palmer", "team": "Chelsea", "goals": 14},
]
    result = top_scoring_teams(players)
    assert result == [('Man City', 37)]

def test_multiple_teams_highest_scores():
    players = [
    {"name": "Salah", "team": "Liverpool", "goals": 18},
    {"name": "Diaz", "team": "Liverpool", "goals": 12},
    {"name": "Haaland", "team": "Man City", "goals": 22},
    {"name": "Foden", "team": "Man City", "goals": 15},
    {"name": "Saka", "team": "Arsenal", "goals": 16},
    {"name": "Odegaard", "team": "Arsenal", "goals": 10},
    {"name": "Palmer", "team": "Chelsea", "goals": 14},
    {"name": "Jose", "team": "Ranches Bee", "goals": 22},
    {"name": "Zion", "team": "Ranches Bee", "goals": 15}
]
    result = top_scoring_teams(players)
    assert result == [('Man City', 37), ('Ranches Bee', 37)]

def test_empty_list():
    assert top_scoring_teams([]) == []
