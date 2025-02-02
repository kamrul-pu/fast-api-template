from fastapi import FastAPI
from app.routes import auth
from app.db.connection import engine, Base

app = FastAPI()

# Include routes
app.include_router(auth.router)


# Create database tables asynchronously
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
