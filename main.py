from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.utils.connect_mongo_db import connectToMongoDB

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to MongoDB
    client = connectToMongoDB()
    db = client["cyvox_db"]
    app.state.db = db
    print("✅ MongoDB client initialized in lifespan.")
    
    # Ensure unique indexes
    test_user_collection = db["users"]
    test_user_collection.create_index("email", unique=True)
    test_user_collection.create_index("phoneNumber", unique=True)
    test_user_collection.create_index("clerkUserId", unique=True)
    print("✅ Unique indexes ensured on email and phoneNumber.")
    
    yield  # control passes to FastAPI here
    client.close()
    print("🧹 MongoDB client closed.")
    

app = FastAPI(title="CyVox Server", lifespan=lifespan)

@app.get("/", tags=["Health-Check"])
def heath_chcek():
    return {"ok": True, "message": "CyVox Server is running!"}

