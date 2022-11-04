import logging

import pandas as pd
from utils.other.pandas_transformations import (clean_columns,
                                                convert_nan_to_None,
                                                convert_to)

logger=logging.getLogger(__name__)

def planning_data_transform(dataframe: pd) -> pd.DataFrame:
    """
    1. Defines the string column characters to replace and the columns
    containg float data types
    2. Pipes a number of transformations to clean the underlying dataset

    Args:
        dataframe (pd): the dataframe to transform

    Returns:
        pd.DataFrame: the cleaned dataframe
    """    
    replace_character_map = {32: 95, 45: 95, 41: "", 40: "", 47: ""}
    float_cols = ["mfo", "mw_energy", "mw_capacity", "mw_in_service"]
    dataframe = (
        dataframe.pipe(clean_columns, character_map=replace_character_map)
        .pipe(
            convert_to,
            columns=[x for x in list(dataframe.head()) if "date" in x],
            dtype="datetime",
        )
        .pipe(convert_to, columns=float_cols, dtype="float")
        .pipe(convert_nan_to_None)
        .assign(county_state=dataframe.county + "," + dataframe.state)
    )
    logger.info("Dataframe cleaned")
    return dataframe
