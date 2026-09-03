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


@pytest.fixture
# Name the fixture function
def prepare_data():
    return [i for i in range(10)]

# Create the tests
def test_elements(prepare_data):
    assert 9 in prepare_data
    assert 10 not in prepare_data

#chain fixture
@pytest.fixture
def list_length():
    return 10

# Define the fixture for a list preparation
@pytest.fixture
def prepare_list(list_length):
    return [i for i in range(list_length)]

def test_9(prepare_list):
    assert 9 in prepare_list
    assert 10 not in prepare_list


#autouse
@pytest.fixture
def init_list():
    return []

# Declare the fixture with autouse
@pytest.fixture(autouse=True)
def add_numbers_to_list(init_list):
    init_list.extend([i for i in range(10)])

# Complete the tests
def test_elementz(init_list):
    assert 1 in init_list
    assert 9 in init_list