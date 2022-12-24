from fastapi import FastAPI

from users import users_endpoints


# API context creation
app = FastAPI(title="Gestor-Finanzas API", version="0.0.1")


# Router
app.include_router(users_endpoints.router)
