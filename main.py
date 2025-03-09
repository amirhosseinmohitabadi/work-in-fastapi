from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return {"message" : "I am amirhossein mohitabadi. I am electrical engineering student at neyshabur university. i am instrested in programming."}

@app.get("/items/{item_id}")
async def read_root(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}