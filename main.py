import uvicorn
from datetime import datetime, timedelta
import schemas, crud
from models import Base
from database import  SessionLocal, engine, Base
from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# Dependency

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

origins = [
    "http://192.168.10.25:8080",
    "http://192.168.10.5:8081",
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def register_exception(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):

        exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
        # or logger.error(f'{exc}')
        logger.error(request, exc_str)
        content = {'status_code': 10422, 'message': exc_str, 'data': None}
        return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@app.post("/api/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db=db,email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}






# Create users
@app.post("/api/add_user/",response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)
     ):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)



@app.get("/api/get_users/",  response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db), current_user: schemas.User = Depends(crud.get_current_active_user)):
    users = crud.get_users(db)
    return users


@app.get("/api/auth/user", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(crud.get_current_active_user)):
    return current_user


@app.get("/api/users/me/items/", response_model=schemas.Renters)
async def read_own_items(current_user: schemas.User = Depends(crud.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.name}]






if __name__ == '__main__':
    uvicorn.run("main:app", host ="0.0.0.0")



