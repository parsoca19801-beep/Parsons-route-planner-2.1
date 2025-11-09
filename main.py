from fastapi import FastAPI
from .routers import health, routes as routes_router, imports as imports_router

app = FastAPI(title="planner-api")
app.include_router(health.router)
app.include_router(routes_router.router)
app.include_router(imports_router.router)
