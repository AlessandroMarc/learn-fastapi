from fastapi import FastAPI
from database import engine
from routers import auth, todos, admin, users
from models import Todos

app = FastAPI()

Todos.metadata.create_all(bind=engine)


@app.get('/healthy')
def health_check():
    return {'status': 'ok'}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
app.include_router(admin.router)
