import uvicorn

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/ping", response_class=PlainTextResponse)
def root():
    return "pong"

@app.get("/hello")
def hello(name: str = "Guest"):
    return PlainTextResponse(f"Hello, {name}!")

@app.post("/count")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) 