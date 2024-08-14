from fastapi import FastAPI,Depends,HTTPException
from db1 import engine,SessionLocal, get_db
import model,schemas,service
from sqlalchemy.orm import Session

models=model.Base.metadata.create_all(bind=engine)

app=FastAPI()



@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if the email is already in use
    existing_user = service.get_user_email(db, user.email)
    # if existing_user:
    #     # Email is already taken, return an error
    #     raise HTTPException(status_code=400, detail=f"Email is already in use {existing_user}")

    # Create a new user since the email is not in use
    new_user = service.create_user(db, user)
    return new_user

@app.get("/user",response_model=list[schemas.User])
def get_users(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    users = service.get_users(db,skip,limit)
    return users

@app.get("/users/{user_id}",response_model=schemas.User)
def get_user(user_id:int,db:Session=Depends(get_db)):
    db_user = service.get_user(db,user_id)
    if db_user is None:
        raise HTTPException(status_code=404 , detail = "User not Found")
    return db_user