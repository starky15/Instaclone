from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_it():
    return "THi si sfun"