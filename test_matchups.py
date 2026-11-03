from matchups import generate_matchups


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
