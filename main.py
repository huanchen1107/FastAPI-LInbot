from typing import Optional
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str]= None 
    price: float
    tax: Optional[float] = None
    

@app.get("/")
def read_root():
    return {"Hello": "World 這是test"}

@app.get("/hello")
def read_root2():
    return {"Hello2": "222 World 這是test"}

################### step 2  Restful API examples ##########
@app.post("/items/")
async def create_item(item: Item):
    return {"Hello2": "222 World 這是test"}

