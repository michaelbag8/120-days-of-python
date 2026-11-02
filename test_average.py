from movies import calculate_average
import pytest

def test_valid_input():
    result = calculate_average([70, 80.6, 90])
    assert result == 80.2

def test_valid_no_float():
    result = calculate_average([50,30, 40])
    assert result == 40.0

def test_invalid_input():
    with pytest.raises(ValueError, match="Scores must contain only numbers"):
        calculate_average([40, True, 50])

def test_empty_input():
    with pytest.raises(ValueError, match="Scores cannot be empty"):
        calculate_average([])