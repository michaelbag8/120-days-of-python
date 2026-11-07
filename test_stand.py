from stand import calculate_league_standings
import pytest


def test_atomicity():
    matches = [
    {"home": "Arsenal", "away": "Liverpool", "home_goals": 2, "away_goals": 0},
    {"home": "Chelsea", "away": "Chelsea", "home_goals": 1, "away_goals": 1}
]
    original_standings = {
    "Arsenal": 6,
    "Chelsea": 3
}

    with pytest.raises(ValueError, match="A team cannot play against itself"):
        calculate_league_standings(matches, original_standings)


def test_normal_input():
    matches = [
    {"home": "Arsenal", "away": "Liverpool", "home_goals": 2, "away_goals": 0},
    {"home": "Chelsea", "away": "Man City", "home_goals": 1, "away_goals": 1}
]
    original_standings = {
    "Arsenal": 6,
    "Chelsea": 3
}

    result = calculate_league_standings(matches, original_standings)
    assert result == {'Arsenal': 9, 'Chelsea': 4, 'Liverpool': 0, 'Man City': 1}