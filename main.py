from fastapi import FastAPI
from setup import setup
from users import users_endpoints, jwt_auth
from labels import labels_endpoints


# API context creation
app = FastAPI(title="Gestor-Finanzas API", version=setup.version)


# Router
app.include_router(users_endpoints.router)
# app.include_router(labels_endpoints)
app.include_router(jwt_auth.router)
