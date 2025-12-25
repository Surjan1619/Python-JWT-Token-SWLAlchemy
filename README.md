>#  __Python (JWT Token, SWLAlchemy) HTML,JS__
> ___
>> __Demonstrational Web Project with JWT and SQLite__\
      A demonstration FastAPI project featuring:\
       JWT authentication for secure login.\
       SQLite database managed with SQLAlchemy.\
       Static HTML pages for main, login, registration, and logged-in views.\
       Token verification endpoints for protected access.\
>
>>- [X] Key Features\   
 User registration and login with JWT tokens.\
        Secured endpoints with token verification.\
        SQLite + SQLAlchemy for user data.\
        Serving static HTML pages with FastAPI.\
>
>>- [X] Tech Stack\
        Backend: FastAPI\
        Auth: JWT (PyJWT / python-jose)\
        Database: SQLite via SQLAlchemy\
        Frontend: Static HTML + JavaScript\
>
>>- [X] Endpoints
Method	Endpoint	Description\
GET _ / _ #Main page\
GET _ /register _ #Registration page\
GET _ /login _#Login page\
POST _ /post_register _ #Register new user\
POST _ /post-login	  _ #Login and get JWT\
GET _ /check-token	_ #Verify JWT token
