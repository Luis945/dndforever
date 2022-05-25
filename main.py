from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def name():
 return {"Welcome":"bienvenido a dndforever"}