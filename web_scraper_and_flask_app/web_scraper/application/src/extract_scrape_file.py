
import logging

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.scraping import download_file_check, download_manager_check

logger=logging.getLogger(__name__)

def scrape_xls_file(url:str, web_driver_path:str,download_path:str,element_xpath:str) -> str:
    """
    1. Sets the preferences and options for the chrome driver
    2. Creates a virtual display
    3. Instantiates the chrome driver and loads the given page in a
    headless browser
    4. Waits for the page to load and then locates the given html element
    5. Selects the given html element to download the desired file
    6. Closes the driver and returns the downloaded file name

    Args:
        url (str): the url of the page to scrape
        web_driver_path (str): path to the web driver
        download_path (str): directory path for browser downloads
        element_xpath (str): xpath for the desired element

    Returns:
        str: name of downloaded file
    """    
    prefs = {
        "profile.default_content_settings.popups": 0,
        "download.default_directory": download_path,  ### Set the path accordingly
        "download.prompt_for_download": False,  ## change the downpath accordingly
        "download.directory_upgrade": True,
    }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option("prefs", prefs)

    
    display = Display(visible=0, size=(1024, 768))
    display.start()
    driver = webdriver.Chrome(web_driver_path, chrome_options=chrome_options)
    file_name=""
    try:
        logger.info("Scraping data")
        driver.get(url)
        element = WebDriverWait(driver, 20).until(
            (
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        element_xpath,
                    )
                )
            )
        )
    
        driver.execute_script("arguments[0].click();", element)
        if not driver.execute_script("return navigator.plugins.length == 0"):
            file_name, driver = download_manager_check.get_file_dl_file_name(driver, 30)
        else:
            file_name = download_file_check.download_wait(
                download_path
            )
    except Exception as err:
        logger.error(err)
    finally:
        driver.close
    return file_name
