import uvicorn


from fastapi import FastAPI, Request, Header, status
from fastapi.responses import PlainTextResponse, RedirectResponse
from starlette.exceptions import HTTPException

app = FastAPI()

# Exercise 1
@app.get("/ping", response_class=PlainTextResponse)
def root():
    return "pong"

# Exercise 2
@app.get("/hello", response_class=PlainTextResponse)
def hello(name: str = "Guest"):
    return f"Hello, {name}!"

# Exercise 3
@app.post("/count", response_class=PlainTextResponse)
async def count(request: Request):
    body = await request.body()
    return str(len(body))

# For the Get response i need to create a FastAPI exception handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 405:
        return PlainTextResponse (
            "Send a POST request",
            status_code=405
        )
    return PlainTextResponse(
        str(exc.detail),
        status_code=exc.status_code
    )
# Exercise 4
@app.get("/calculate")
def calculate(a: str, b: str, op: str) -> str:
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Bad Request"
        )
    if op == "add":
        return f"Result: {a + b}"
    
    elif op == "subtract":
        return f"Result: {a - b}"

    elif op == "multiply":
        return f"Result: {a * b}"

    raise HTTPException(
        status_code=400,
        detail="Bad Request"
    )

# Excercise 5
@app.get("/agent")
def agent(user_agent: str | None = Header(default=None)):
    return f"You are visiting us using: {user_agent}"

@app.get("/dashboard")
def dashboard(x_api_key: str | None = Header(default=None)):
    if x_api_key != "secret123":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return "Welcome"


@app.get("/legacy")
def legacy():
    return RedirectResponse(url="/v2", status_code=status.HTTP_301_MOVED_PERMANENTLY)

@app.get("/v2", response_class=PlainTextResponse)
def version_two():
    return "Welcome to version 2"

# The Strectch using Depends() --> check it out
# def verify_api_key(x_api_key: str | None = Header(default=None)):
#     if x_api_key != "secret123":
#         raise HTTPException(
#             status_code=401,
#             detail="Unauthorized"
#         )

# @app.get("/dashboard")
# def dashboard(api_key: str = Depends(verify_api_key)):
#     return "Welcome to the dashboard!"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) 