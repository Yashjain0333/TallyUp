import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import os

from api.routes.users import user_router

# Uncomment to connect MongoDB before startup
@asynccontextmanager
async def _lifespan(app:FastAPI):
    # app.mongodb_client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    # app.mongodb = app.mongodb_client[os.getenv("MONGO_DB", "mobile_app")]
    # print("Connected to MongoDB")
    yield
    # app.mongodb_client.close()
    # print("MongoDB connection closed")

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

app.include_router(user_router,prefix='/user',tags=['User'])

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
