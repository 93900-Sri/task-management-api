from fastapi import FastAPI
from routers.users import router as users_router
from routers.tasks import router as tasks_router

app = FastAPI(title="Task Management API", version="1.0.0")
app.include_router(users_router)
app.include_router(tasks_router)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
