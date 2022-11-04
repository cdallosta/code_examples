import logging
import os

import pandas as pd
from config import Config
from src.extract_location_data import location_data_pull
from src.extract_scrape_file import scrape_xls_file
from src.load_pjm_data import insert_to_postgres
from src.transform_combine_data import pjm_data_upload_prep
from src.transform_xlsx_data import planning_data_transform
from utils.database.postgres import PostgresOperations
from utils.other.clear_directory import rm_directory_file
from utils.other.log import setup_logger

root_path = str(os.path.abspath(os.path.join(__file__,os.pardir)))
web_driver_path =root_path+Config.WEB_DRIVER_PATH
download_path = root_path+Config.WEB_DRIVER_DOWNLOAD_PATH
log_path = root_path+Config.LOG_PATH
root_logger = setup_logger(log_path)
root_logger.info("My Logger has been initialized")
postgres = PostgresOperations( Config.POSTGRES_HOST,
    Config.POSTGRES_PORT,
    Config.POSTGRES_USERNAME,
    Config.POSTGRES_PASSWORD,
    Config.POSTGRES_DB)

if not postgres.test_connect():
    message = "Unable to connect to database. Exiting"
    raise SystemError(message)



rm_directory_file(download_path)
file_name = scrape_xls_file(Config.SITE_URL,web_driver_path,download_path, Config.SITE_ELEMENT_XPATH)
download_file_path = os.path.join(download_path, file_name)
planning_df = pd.read_excel(
    download_file_path,
    sheet_name=Config.EXCEL_SHEET_NAME,
)
planning_df = pd.read_excel(download_file_path, sheet_name=Config.EXCEL_SHEET_NAME)
cleaned_planning_df = planning_data_transform(planning_df)
location_df, errors = location_data_pull(
    cleaned_planning_df, Config.GEOCODE_API_KEY, Config.IO_THREADS
)

merged_df = pjm_data_upload_prep(
    cleaned_planning_df, location_df
)
insert_to_postgres(
    Config.POSTGRES_HOST,
    Config.POSTGRES_PORT,
    Config.POSTGRES_USERNAME,
    Config.POSTGRES_PASSWORD,
    Config.POSTGRES_DB,
    Config.POSTGRES_TABLE_NAME,
    merged_df,
)
   
