from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def getMail():
    return "Hello This is your email getter"