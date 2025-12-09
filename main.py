from fastapi import FastAPI
from app.api.v1.endpoints import items
from app.db.session import engine, Base

# Create tables (use Alembic for production migrations instead)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD Project")

# Include Router
app.include_router(items.router, prefix="/api/v1/items", tags=["Items"])

@app.get("/hello")
def root():
    return {"message": "Server is running"}
