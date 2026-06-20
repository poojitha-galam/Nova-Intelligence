from pymongo import (
    MongoClient
)
from backend.config import (
    config
)
client = MongoClient(
    config.MONGO_URI
)
db = client[
    config.DATABASE_NAME
]
candidate_collection = db[
    "candidates"
]
job_collection = db[
    "jobs"
]
ranking_collection = db[
    "rankings"
]
analytics_collection = db[
    "analytics"
]