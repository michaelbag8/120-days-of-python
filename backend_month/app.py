
def generate_task_id(tasks: list[dict]) -> int:
    if not tasks:
        return 1
    
    return max(task["id"] for task in tasks) + 1
    

def create_task(title: str, task_id: int, tasks: list[dict]) -> dict:
    if not isinstance(title, str):
        raise TypeError("Title can only be string")


    if isinstance(task_id, bool) or not isinstance(task_id, int):
        raise TypeError("Task ID must be an integer")
    
    
    if task_id <= 0:
        raise ValueError("Task ID must be greater than zero")
    
    if not title.strip():
        raise ValueError("Task title cannot be empty")
    
    
    for task in tasks:
        if task_id == task["id"]:
            raise ValueError("ID already exist")
        
    new_task = {
        "id": task_id,
        "title": title,
        "completed": False
    }

    tasks.append(new_task)
    return new_task

class TaskNotFoundError(Exception):
    pass

def find_task(task_id: int, tasks: list[dict]) -> dict:
    for task in tasks:
        if task_id == task["id"]:
            return task
       
    raise TaskNotFoundError("Task not found")