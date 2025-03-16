"""Main Module for FastAPI Server
"""
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
import os

from database.database import initiate_database, close_database

from api.routes.users import user_router
from api.routes.xpense import xpense_router
from api.routes.auth import auth_router


# Uncomment to connect MongoDB before startup
@asynccontextmanager
async def _lifespan(app: FastAPI):
    await initiate_database()
    print("Connected to MongoDB")
    yield
    await close_database()
    print("MongoDB connection closed")


app = FastAPI(
    title="TallyUp Backend API",
    description="Backend API for Android/iOS mobile application",
    version="0.1.0",
    lifespan=_lifespan,
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["User"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(xpense_router, prefix="/xpense", tags=["Expense"])


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
