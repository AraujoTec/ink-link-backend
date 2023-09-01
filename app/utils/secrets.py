import os

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")
DB_NAME = os.getenv("DB_NAME", "ink-link")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_URL = os.getenv("DB_URL", "postgresql://postgres:postgres@localhost:5432/ink-link")
ENVIROMENT = os.getenv("ENVIROMENT")