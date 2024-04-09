from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://Abhishek676062:Akshay676062@library.wnsobvz.mongodb.net/?retryWrites=true&w=majority&appName=library"

client = AsyncIOMotorClient(MONGO_URI)
db = client.get_database("library")
students_collection = db.get_collection("students")