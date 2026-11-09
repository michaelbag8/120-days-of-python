from stand import calculate_league_standings
import pytest


def test_atomicity():
    matches = [
        {"match_id":"M001", "home": "Arsenal", "away": "Liverpool", "home_goals": 2, "away_goals": 0},
        {"match_id":"M002", "home": "Chelsea", "away": "Chelsea", "home_goals": 1, "away_goals": 1}
    ]

    original_standings = {
        "Arsenal": 6,
        "Chelsea": 3
    }
    processed_matches = set()

    with pytest.raises(ValueError, match="A team cannot play against itself"):
        calculate_league_standings(matches, original_standings, processed_matches)


def test_calculate_league_standings_success():
    matches = [
        {"match_id":"M001", "home": "Arsenal", "away": "Liverpool", "home_goals": 2, "away_goals": 0},
        {"match_id":"M002", "home": "Chelsea", "away": "Man City", "home_goals": 1, "away_goals": 1}
    ]

    original_standings = {
        "Arsenal": 6,
        "Chelsea": 3
    }
    processed_matches = set()

    result = calculate_league_standings(matches, original_standings, processed_matches)

    assert result == {
        "Arsenal": 9,
        "Chelsea": 4,
        "Liverpool": 0,
        "Man City": 1
    }


def test_check_against_original():
    matches = [
        {"match_id":"M001", "home": "Arsenal", "away": "Liverpool", "home_goals": 2, "away_goals": 0},
        {"match_id":"M002", "home": "Chelsea", "away": "Man City", "home_goals": 1, "away_goals": 1}
    ]

    original_standings = {
        "Arsenal": 6,
        "Chelsea": 3
    }
    processed_matches = set()

    result = calculate_league_standings(matches, original_standings, processed_matches)

    assert original_standings == result
    assert processed_matches == {"M001", "M002"}


def test_standings_remain_unchanged_when_match_is_invalid():
    original_standings = {
        "Arsenal": 6,
        "Chelsea": 3
    }

    original_copy = original_standings.copy()

    matches = [
        {"match_id":"M001", "home": "Arsenal", "away": "Liverpool", "home_goals": 2, "away_goals": 0},
        {"match_id":"M002", "home": "Chelsea", "away": "Chelsea", "home_goals": 1, "away_goals": 1}
    ]

    processed_matches = set()

    with pytest.raises(ValueError):
        calculate_league_standings(matches, original_standings, processed_matches)

    assert original_standings == original_copy
    assert processed_matches == set()

def test_reject_previously_processed_match():
    processed_matches = {"M001"}
    processed_matches_copy = processed_matches.copy()

    matches = [
        {
        "match_id": "M001",
        "home": "Arsenal",
        "away": "Chelsea",
        "home_goals": 2,
        "away_goals": 0
        }
    ]

    original_standings = {"Arsenal": 6, "Chelsea": 3}
    with pytest.raises(ValueError):
        calculate_league_standings(matches, original_standings, processed_matches)
    assert processed_matches == processed_matches_copy