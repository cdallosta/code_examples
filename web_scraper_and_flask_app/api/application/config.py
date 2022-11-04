from os import getenv

from dotenv import find_dotenv, load_dotenv


class Config:
    load_dotenv(find_dotenv())
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_POOL_SIZE = getenv("SQLALCHEMY_POOL_SIZE")
    SQLALCHEMY_MAX_OVERFLOW = getenv("SQLALCHEMY_MAX_OVERFLOW")
    SQLALCHEMY_POOL_RECYCLE = getenv("SQLALCHEMY_POOL_RECYCLE")
    LOG_PATH = getenv("LOG_PATH")
    LOG_FORMAT = getenv("LOG_FORMAT")
