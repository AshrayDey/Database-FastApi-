import model,schemas
from sqlalchemy.orm import Session

#get user by id
def get_user(db:Session,user_id):
    return db.query(model.User).filter(model.User.id == user_id).first()

#get user by email
def get_user_email(db:Session,email):
    return db.query(model.User).filter(model.User.email == email)

#get all users
def get_users(db:Session, skip:int=0, limit:int=100):
    return db.query(model.User).offset(skip).limit(limit).all()

#create user
def create_user(db:Session , user:schemas.UserCreate):
    hashed_password = user.password + "hash"

    db_user= model.User(
        email=user.email,
        hashed_password=hashed_password,
        is_active=True
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user) 
    return db_user

#get items
def get_items(db:Session , skip:int = 0, limit:int=100):
    return db.query(model.Item).offset(skip).limit(limit).all()

#get items of a user
def get_items_byUser(db:Session , user_id ):
    return db.query(model.Item).filter(model.Item.owner_id == user_id).all()

#create item
def create_item(db:Session,item:schemas.ItemBase,user_id:int):
    db_item=model.Item(
        title=item.title,
        description=item.description,
        owner_id=user_id
    )

    db.add(db_item)
    db.commit
    return db_item
