from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine, Base
from routes.user import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create all tables on startup
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="FastAPI",
    description="FastAPI",
    lifespan=lifespan,
)

# Include routers
app.include_router(user_router)


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
