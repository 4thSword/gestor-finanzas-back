from fastapi import FastAPI
from routers import users
from routers import jwt_auth
from routers import labels


# API context creation
app = FastAPI(title="Gestor-Finanzas API", version="0.0.1")


# Router
app.include_router(users.router)
app.include_router(labels.router)
app.include_router(jwt_auth.router)
