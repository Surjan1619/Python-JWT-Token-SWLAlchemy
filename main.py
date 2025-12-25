from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from tools import create_access_token, verify_token, get_user, add_user
from tools import UserCreate, User
from pathlib import Path
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")




@app.get("/")
async def main_page():
    return FileResponse(STATIC_DIR / "main_page.html")



@app.get("/register")
async def  register():

    return FileResponse(STATIC_DIR / "register_page.html")



@app.get("/login")
async def login():
    return FileResponse(STATIC_DIR / "login_page.html")


@app.get("/loged")
async def loged():
    return FileResponse(STATIC_DIR / "loged.html")



@app.post("/post_register")
async def post_register(user: UserCreate):

    user = User(username=user.username, password=user.password)

    if add_user(user):
        return {"status": "ok"}
    else:
        return HTTPException(status_code=400, detail="Incorrect username or password")




@app.post("/post-login")
async def post_login(user: UserCreate):
    result = get_user(user)
    if result is False:
        raise HTTPException(status_code=401, detail="User not found")
    else:
        token = create_access_token({"sub": user.username})
        return {"status": "ok",
                "access_token": token}


@app.get("/check-token")
async def check_token(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    print("ohayo")
    if payload:
        return {"status": "ok",
                "username" : payload["sub"]}
    else:
        print("ohayo")
        raise HTTPException(status_code=401, detail="Invalid token")


"""if the user is already logged in
 he can press the bottom "Перейти дальше" and after the browser is doing get request to verify his token
 and if an answer is true he can move forward"""
