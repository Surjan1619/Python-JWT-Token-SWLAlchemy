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
GET____/________________#Main page\
GET ____ /register ________#Registration page\
GET ____ /login __________#Login page\
POST ___ /post_register ___ #Register new user\
POST ___ /post-login	   ______ #Login and get JWT\
GET ____ /check-token	_____#Verify JWT token
