import pytest
from datetime import datetime

def multiple_of_two(num):
    if num == 0:
        raise(ValueError)
    return num % 2 == 0

def test_numbers():
    # Write the "True" test below
    assert multiple_of_two(2) == True

def test_number():
    assert multiple_of_two(3) == False

# To skip a test using a decorator
@pytest.mark.skip
def test_zero():    
  	# Add a context for an exception test here
    with pytest.raises(ValueError):
      	# Check zero input below
        multiple_of_two(0)

@pytest.mark.xfails
def test_fails():
    # Write any assert test that will fail
    assert multiple_of_two(7) == False


day_of_week = datetime.now().isoweekday()

def get_unique_values(lst):
    return list(set(lst))

condition_string = 'day_of_week == 6'
# Add the conditional skip marker and the string here
@pytest.mark.skipif(condition_string, reason="Skipped on Saturdays")
def test_function():
	# Complete the assertion tests here
    assert get_unique_values([1,2,3]) == [1,2,3]
    assert get_unique_values([1,2,3,1]) == [1,2,3]