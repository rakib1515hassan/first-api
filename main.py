from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, World! This is my first API!"}


@app.get("/v2/landing-page")
def LandingPageApi():
    response = {
        "slug": "samsung-s26-ultra-hot-sale"
    }
    return response
