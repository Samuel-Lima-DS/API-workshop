from fastapi import FastAPI

app = FastAPI()


@app.get("/")  #request
def ola_mundo(): #response 
    return {"ola": "mundo"}

