from typing import Any, Dict


def item_generator(json_input: Dict[str, Any], lookup_key: str) -> Any:
    """Recursively iterates through a dictionary looking
    for a given key. When found, returns the key value

    Args:
        json_input (Dict[str, Any]): the dictionary input
        lookup_key (str): the key to look for

    Yields:
        Any: the value for the given key
    """
    if isinstance(json_input, dict):
        for key, value in json_input.items():
            if key == lookup_key:
                yield value
            else:
                yield from item_generator(value, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)
