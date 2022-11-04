from typing import Any, Dict, List, Union

import numpy as np
import pandas as pd


def convert_nan_to_None(dataframe: pd, columns: List[Any] = []) -> pd.DataFrame:
    """_summary_

    Args:
        dataframe (pd): dataframe to convert class specifc nulls to None type
        columns (List[Any], optional): columns within the dataframe to convert values
        to None type.
        Defaults to [].

    Returns:
        (pd.DataFrame): the cleaned dataframe
    """    
    if not columns:
        columns = list(dataframe.head())

    dataframe[columns] = dataframe[columns].replace(
        {np.NaN: None, pd.NaT: None, "": None, "N/A": None}
    )
    return dataframe


def clean_strings(
    input: Union[List, str], character_map: Dict[str, str] = {}, lower: bool = False
) -> Union[List, str]:
    """
    1. Performs strip, translate, and lower (when indicated) by data types

    Args:
        input (Union[List, str]): the object to clean
        character_map (Dict[str, str], optional): the character map for translate.
        Defaults to {}.
        lower (bool, optional): Whether to lower the case of the input.
        Defaults to False.

    Returns:
        Union[List, str]: cleaned input
    """
    def clean(input):
        if lower:
            return input.lower().strip().translate(character_map)
        return input.strip().translate(character_map)

    if isinstance(input, str):
        return clean(input)
    elif isinstance(input, list):
        return list(map(lambda x: clean(x), input))



def clean_columns(dataframe: pd.DataFrame, character_map: Dict[str, Any])->pd.DataFrame:
    """
    Replaces characters and lowers the case of the columns for a dataframe

    Args:
        dataframe (pd.DataFrame): the dataframe
        character_map (Dict[str, Any]): the character map for translate

    Returns:
        pd.DataFrame: dataframe with cleaned columns
    """
    columns = list(dataframe.head())
    cleaned_columns = clean_strings(columns, character_map, True)
    dataframe.columns = cleaned_columns
    return dataframe


def convert_to(
    dataframe: pd.DataFrame, columns: List[str], dtype: str, convert_none: bool = False
) -> pd.DataFrame:
    """
    Converts column(s) to the desired datatype (str, int, float, datetime, date). Will
    also convert null values to Nonetype

    Args:
        dataframe (pd): the dataframe to set the datatype
        columns (List[str]): the columns to convert the dtype
        dtype (str): the desired data type
        convert_none (bool, optional): Boolean to determine if the class specific none types
        are to be converted to Nonetype. Defaults to False.

    Returns:
        pd.DataFrame: the cleaned dataframe
    """
    if dtype == "str":
        dataframe[columns] = dataframe[columns].astype(str)
    elif dtype == "int":
        dataframe[columns] = dataframe[columns].astype(int)
    elif dtype == "float":
        dataframe[columns] = dataframe[columns].astype(float)
    elif dtype == "datetime":
        dataframe[columns] = dataframe[columns].apply(pd.to_datetime)
    elif dtype == "date":
        dataframe[columns] = dataframe[columns].apply(
            lambda x: pd.to_datetime(x, errors="coerce", format="%d/%m/%Y").dt.date
        )

    if convert_none:
        dataframe = convert_nan_to_None(columns, dataframe)
    return dataframe
