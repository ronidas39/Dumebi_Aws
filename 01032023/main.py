from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/index")
def root():
    return {"message": "this is index endpoint"}


@app.get("/sum")
def root():
    a=10
    b=20
    return {"message": str(a+b)}