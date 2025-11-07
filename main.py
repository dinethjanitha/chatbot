from typing import Union
from fastapi import FastAPI

from agents.tools import call_agent

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}


@app.post("/api/v1/chat")
def read_item(prompt : str):
    return call_agent(prompt)