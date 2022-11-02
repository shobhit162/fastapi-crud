from fastapi import FastAPI
from routes.todos_routes import user
app = FastAPI()
app.include_router(user)
