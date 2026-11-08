from app import create_task, find_task, TaskNotFoundError, generate_task_id, DuplicateTaskError

import pytest

def test_new_task_valid_input():
    tasks = [
    {"id": 1, "title": "Learn Python"},
    {"id": 2, "title": "Learn FastAPI"},
    {"id": 3, "title": "Practise SQL"}
]
    result = create_task("Learn MongoDB", 4, tasks)
    assert result == {'id': 4, 'title': 'Learn MongoDB', 'completed': False}

def test_tasks_valid_input():
    tasks = [
    {"id": 1, "title": "Learn Python"},
    {"id": 2, "title": "Learn FastAPI"},
    {"id": 3, "title": "Practise SQL"}
]
    _ = create_task("Learn MongoDB", 4, tasks)
    assert tasks == [{'id': 1, 'title': 'Learn Python'}, {'id': 2, 'title': 'Learn FastAPI'}, {'id': 3, 'title': 'Practise SQL'}, {'id': 4, 'title': 'Learn MongoDB', 'completed': False}]


def test_duplicate_id_input():
    tasks = [
    {"id": 1, "title": "Learn Python"},
    {"id": 2, "title": "Learn FastAPI"},
    {"id": 3, "title": "Practise SQL"}
]
    with pytest.raises(DuplicateTaskError, match="ID already exist"):
        create_task("Learn Java", 3, tasks)
    

def test_empty_title_input():
    tasks = [
        {"id": 1, "title": "Learn Python"}
    ]
    with pytest.raises(ValueError,match="Task title cannot be empty"):
        create_task("", 2, tasks)

    
def test_boolean_id_input():
    tasks = [
    {"id": 1, "title": "Learn Python"},
    ]
    with pytest.raises(TypeError, match="Task ID must be an integer"):
        create_task("Learn Django", True, tasks)

def test_non_int_id_title():
    tasks = [
    {"id": 1, "title": "Learn Python"},
    ]
    with pytest.raises(TypeError, match="Task ID must be an integer"):
        create_task("Learn Swimming", "2", tasks)

def test_non_string_title():
    tasks = [
    {"id": 1, "title": "Learn Python"},
    ]
    with pytest.raises(TypeError, match="Title can only be string"):
        create_task(12345, 2, tasks)

def test_negative_task_id():
    tasks = [
    {"id": 1, "title": "Learn Python"},
    ]
    with pytest.raises(ValueError, match="Task ID must be greater than zero"):
        create_task("Learn To Play Guitar", -2, tasks)
    
def test_zero_task_id():
    tasks = [
    {"id": 1, "title": "Learn Python"},
    ]
    with pytest.raises(ValueError, match="Task ID must be greater than zero"):
        create_task("Learn To Sing", 0, tasks)


def test_find_task_returns_existing_task():
    tasks = [
        {"id": 1, "title": "Learn Python"},
        {"id": 2, "title": "Learn FastAPI"}
    ]

    result = find_task(2, tasks)

    assert result == {"id": 2, "title": "Learn FastAPI"}



def test_find_task_raises_error_when_task_does_not_exist():
    tasks = [
        {"id": 1, "title": "Learn Python"},
        {"id": 2, "title": "Learn FastAPI"}
    ]

    with pytest.raises(TaskNotFoundError):
        find_task(5, tasks)

def test_find_task_error_message():
    tasks = []

    with pytest.raises(TaskNotFoundError, match="Task not found"):
        find_task(5, tasks)

def test_empty_generate_id():
    assert generate_task_id([]) == 1
    
