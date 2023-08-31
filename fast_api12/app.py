from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def add_numbers(x: int, y: int):
    result = x + y
    return {"result": result}
