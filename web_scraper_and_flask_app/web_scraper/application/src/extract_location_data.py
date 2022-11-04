
import logging
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Tuple

import pandas as pd
from utils.api_requests.request import get
from utils.other.json_key_recursion import item_generator

logger=logging.getLogger(__name__)

def location_data_pull(data: pd.DataFrame, api_key: str, threads: int = 4) -> Tuple[pd.DataFrame, List[str]]:
    """
    1. Takes in a dataframe containing the pjm data set
    2. Extracts a unique list county/states
    3. Passes the county/state list to the get_lat_long callable. Using threading
    to accelerate the IO process
    4. Removes any null values
    5. Creates a dataframe from the GET results
    6. Renames the dataframe columns

    Args:
        data (pd.DataFrame): the dataset by which to extract the necessary
        get query parameters
        api_key (str): the api key for the get request
        threads (int, optional): The number of threads to use for IO operations.
        Defaults to 4.

    Returns:
        Tuple(pd.DataFrame, List[str]): Tuple containing the Dataframe housing the county_state and it's associate 
        latitude/longitude, and a list containing any errors during the GET request
    """    
    errors = []

    def get_lat_long(county_state: str) -> Dict[str,Any]:
        """
        1. Takes in concatenated county state
        2. Splits the string and set the appropriate variables
        3. Prepares the parameters for injection into the request URL
        4. Performs a get request
        5. Uses the item_generator callable to recursively locate the desired
        6. Appends any county/states that experience errors to the errors var
        key
        6. Adds the county_state key to the resulting dictionary

        Args:
            county_state (str): concatenation of county and state

        Returns:
            Dict[str,Any]: the county/state and it's resulting latitude/longitude
        """        
        split_county_state: str = county_state.split(",")
        county: str = split_county_state[0]
        abbrev_state = split_county_state[1]
        url_county = county.replace(" ", "%20")
        url = f"https://api.opencagedata.com/geocode/v1/json?q={url_county}+{abbrev_state}&key={api_key}&pretty=1"
        try:
            response = get(url)
            location_dict = next(item_generator(response, "geometry"))
            location_dict["county_state"] = county_state
            return location_dict
        except Exception as err:
            logger.info(SystemExit(err))
            errors.append(
                {
                    "state_county": county_state,
                    "errors": SystemExit(err),
                }
            )

    county_state_df = data["county"] + "," + data["state"]
    county_state_list = list(county_state_df.dropna().unique())
    #county_state_list = county_state_list[-3:]  # ["asdas,asda"]  #
    result = []
    logger.info("Extracting location data")
    with ThreadPoolExecutor(threads) as executor:
        result = list(executor.map(get_lat_long, county_state_list))

    cleaned_result = [x for x in result if x is not None]
    location_df = pd.DataFrame(
        cleaned_result,
    ).rename(columns={"lat": "latitude", "lng": "longitude"})
    logger.info("Location data extracted")
    return location_df, errors

