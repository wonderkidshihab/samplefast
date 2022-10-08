from fastapi import FastAPI, Depends, HTTPException, status
from Routes.userRoutes import app as userRoutes
from Routes.productRoutes import app as productRoutes
from Routes.categoryRoutes import app as categoryRoutes
import Models
from Database.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(userRoutes)
app.include_router(productRoutes)
app.include_router(categoryRoutes)



@app.get("/")
def sampleHome():
    return {"data": "This is gonna be a sample home page"}
