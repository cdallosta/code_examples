import logging

import pandas as pd
from utils.other.pandas_transformations import convert_nan_to_None

logger=logging.getLogger(__name__)

def pjm_data_upload_prep(pjm_data:pd.DataFrame, location_data: pd.DataFrame ) ->pd.DataFrame:
    """
    1. Outer joins the two given dataframes on the county_state key
    2. Drops the unnecssary concatenated key and sets the primary key
    as the index

    Args:
        pjm_data (pd.DataFrame): pdm dataset
        location_data (pd.DataFrame): location dataset

    Returns:
        (pd.DataFrame): dataframe resulting from the outer join
    """
   
    merged_df = pd.merge(
        pjm_data, location_data, how="outer", on=["county_state", "county_state"]
    )
    merged_df = merged_df.drop("county_state", axis=1).pipe(convert_nan_to_None).set_index("queue_number")
    
    return merged_df

    

