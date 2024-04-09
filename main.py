from fastapi import FastAPI
from database import students_collection

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/students")
async def get_students():
    students = await students_collection.find().to_list(None)
    return [{"id": str(student["_id"]), **{k: v for k, v in student.items() if k != "_id"}} for student in students]

if __name__ == "__main__":
    import uvicorn
    print("Starting the application...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)