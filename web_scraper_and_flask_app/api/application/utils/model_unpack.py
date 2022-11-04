from typing import Any, Dict, List


def dict_helper(objlist:List[Any])->Dict[str,Any]:
    """
    Iterates through a list of SQLAlchemy objects.
    Converts the object to dictionary, removes troublesome keys
    and returns a list of dictionaries

    Args:
        objlist (List[Any]): _description_

    Returns:
        Dict[str,Any]: _description_
    """    
    result_list = []
    for x in objlist:
        obj_dict:dict = x.__dict__
        if "_sa_instance_state" in list(obj_dict.keys()):
            del obj_dict["_sa_instance_state"]
        result_list.append(obj_dict)
    return result_list