import os, dotenv
from typing import Literal

IS_PROD = os.getenv("IS_PROD", False)
if not IS_PROD:
    dotenv.load_dotenv(".env.development")

# ----- [[ DATABASE ]] -----

DB_DRIVER = "postgresql+asyncpg"
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# ----- [[ EMAIL ]] -----

EMAIL_SENDER = os.environ.get("EMAIL_SENDER")
EMAIL_HOSTNAME = os.environ.get("EMAIL_HOSTNAME")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
DB_USER = os.environ.get("DB_USER")
EMAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

# ----- [[ OTHER ]] -----

API_URL = os.environ.get("API_URL")
ROOT_PATH = os.environ.get("ROOT_PATH", "")
