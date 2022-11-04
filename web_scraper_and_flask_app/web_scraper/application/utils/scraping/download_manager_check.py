from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def get_file_dl_file_name(
    driver: webdriver, timeout: int = 120, poll_frequency: int = 1
):
    """Checks if the file has finished downloading via the chrome://downloads
    page

    Args:
        driver (webdriver): the webdriver
        timeout (int, optional): how long to wait for download to complete. Defaults to 120.
        poll_frequency (int, optional): how frequently to poll for download completion.
        Defaults to 1.
    """
    def chrome_downloads(driver: webdriver, timeout: int = 120) ->str:
        """Polls chrome://downloads for file download completion

        Args:
            driver (webdriver): the webdriver
            timeout (int, optional): how long to wait for download to complete. Defaults to 120.. Defaults to 120.

        Returns:
            str: the filename of the download
        """
        if (
            not "chrome://downloads" in driver.current_url
        ): 
            driver.execute_script("window.open()")
            sleep(5)
            driver.switch_to.window(driver.window_handles[1])
            driver.get("chrome://downloads/")
            for _ in range(0, timeout, 1):
                try:
                    download_percentage = driver.execute_script(
                        "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('#progress').value"
                    )
                    if download_percentage == 100:
                        file_name = driver.execute_script(
                            "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text"
                        )
                        return file_name
                except:
                    pass
                sleep(1)

    file_name = WebDriverWait(driver, timeout, poll_frequency).until(
        chrome_downloads
    )
    if "chrome://downloads" in driver.current_url:
        driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return file_name, driver
