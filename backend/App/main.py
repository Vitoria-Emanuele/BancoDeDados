from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "minha api esta no ar"
