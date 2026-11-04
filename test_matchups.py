from matchups import generate_matchups, group_players_by_team


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