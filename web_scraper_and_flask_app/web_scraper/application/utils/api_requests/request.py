from json import JSONDecodeError
from typing import Any, Dict

import requests


def get(url: str, *args, **kwargs) -> Dict[str, Any]:
    """
    Takes in the url and additional args/kwargs. Performs a
    get request and returns the results as a dictionary.

    Args:
        url (str): _description_

    Raises:
        SystemExit: returns the request exception
        SystemExit: returns the json decode exception

    Returns:
        Dict[str, Any]: response as a dictionary
    """
    try:
        response = requests.get(url=url, headers=kwargs)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    if response.ok:
        try:
            response_dict = response.json()
        except JSONDecodeError as e:
            raise SystemExit(e)
        return response_dict
    else:
        response.raise_for_status()
