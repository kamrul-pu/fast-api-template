from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth
from app.db import base, session

# Create FastAPI app
app = FastAPI()

# CORS middleware setup (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include authentication routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/")
def index():
    return {"Name": "My App", "version": "1.0"}


# Create tables on startup (using Alembic is recommended, but this works for simple cases)
@app.on_event("startup")
def on_startup():
    base.Base.metadata.create_all(bind=session.engine)
