"""Main Module for FastAPI Server"""

import os
import logging
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from middlewares.single_quote_parser import SingleQuoteJSONMiddleware
from database.database import initiate_database, close_database

from api.routes.users import user_router
from api.routes.xpense import xpense_router
from api.routes.auth import auth_router

logging.basicConfig(level=logging.INFO, format="%(levelname)s: \t  %(message)s")
logger = logging.getLogger("main")


@asynccontextmanager
async def _lifespan(app: FastAPI):
    await initiate_database()
    logger.info("Connected to MongoDB")
    yield
    await close_database()
    logger.info("MongoDB connection closed")


app = FastAPI(
    title="TallyUp Backend API",
    description="Backend API for Android/iOS mobile application",
    version="0.1.0",
    lifespan=_lifespan,
)

app.add_middleware(SingleQuoteJSONMiddleware)
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
