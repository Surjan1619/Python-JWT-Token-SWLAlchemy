
import jwt
from jose import jwt
from datetime import datetime, timedelta
from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session
from pydantic import BaseModel


SECRET_KEY = "key example" #i need to save the key into #env file but it's heare to show you how it works
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5
engine = create_engine("sqlite:///database.db", echo=False)


"""classs to validate and work with ORM"""
class UserCreate(BaseModel):
    username : str
    password : str


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(100), nullable=False)


"""creating token"""
def create_access_token(data:dict, expires_delta: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode  = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

"""verifying token with each request"""
def verify_token(token):
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

"""geting user from DB  and if """
def get_user(user):
    try:

        Session = sessionmaker(bind=engine)
        session = Session()
        user = User(username=user.username, password=user.password)
        if session.query(User).filter(User.username == user.username, User.password == user.password).first():
            return True
        else:
            return False
    except:
        raise "Something went wrong check get_user_pack"
    finally:
        session.close()

def add_user(user : User):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(user)
        session.commit()
        return {
            "status": "ok"
        }
    except Exception as e:
        session.rollback()
        print(e)
    finally:
        session.close()

