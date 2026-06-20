import os
class Config:
    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017"
    )
    DATABASE_NAME = "talentsphere"
    EMBEDDING_MODEL = (
        "sentence-transformers/"
        "all-MiniLM-L6-v2"
    )
    TOP_K_RESULTS = 20
    SEMANTIC_WEIGHT = 0.35
    SKILL_WEIGHT = 0.25
    EXPERIENCE_WEIGHT = 0.20
    PROJECT_WEIGHT = 0.10
    CERTIFICATION_WEIGHT = 0.05
    EDUCATION_WEIGHT = 0.05
    FRAUD_THRESHOLD = 0.70
    DEBUG = True
    SECRET_KEY = (
        "talentsphere-secret-key"
    )
config = Config()