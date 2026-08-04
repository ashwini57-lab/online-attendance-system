import os
from pymongo import MongoClient

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://mongo:27017"
)

client = MongoClient(MONGO_URI)

db = client["attendance_db"]

users = db["users"]

students = db["students"]

teachers = db["teachers"]

attendance = db["attendance"]

leave_requests = db["leave_requests"]