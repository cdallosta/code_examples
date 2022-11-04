from os import environ, getenv

from dotenv import find_dotenv, load_dotenv


class Config:
    load_dotenv(find_dotenv())
    WEB_DRIVER_PATH = getenv("WEB_DRIVER_PATH")
    WEB_DRIVER_DOWNLOAD_PATH = getenv("WEB_DRIVER_DOWNLOAD_PATH")
    SITE_ELEMENT_XPATH = getenv("SITE_ELEMENT_XPATH")
    SITE_URL = getenv("SITE_URL")
    GEOCODE_API_KEY = getenv("GEOCODE_API_KEY")
    EXCEL_SHEET_NAME = getenv("EXCEL_SHEET_NAME")
    IO_THREADS = int(getenv("IO_THREADS"))
    POSTGRES_HOST = getenv("POSTGRES_HOST")
    POSTGRES_PORT = getenv("POSTGRES_PORT")
    POSTGRES_USERNAME = getenv("POSTGRES_USERNAME")
    POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = getenv("POSTGRES_DB")
    POSTGRES_TABLE_NAME = getenv("POSTGRES_TABLE_NAME")
    LOG_PATH = getenv("LOG_PATH")
    LOG_FORMAT= getenv("LOG_FORMAT")
