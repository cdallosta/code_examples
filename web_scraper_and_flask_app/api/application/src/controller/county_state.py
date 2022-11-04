from typing import Any, Dict

from sqlalchemy import func
from src.models.county_state import PJMProjectsModel
from utils.model_unpack import dict_helper


def projects_by_county(county: str)->Dict[str, Any]:
    """Queries backend db to return results by county

    Args:
        county (str): the county to filter by

    Returns:
        Dict[str, Any]: the results
    """
    results =  PJMProjectsModel.query.filter(
        func.lower(PJMProjectsModel.county) == county.lower()
    ).all()
    return dict_helper(results)

def projects_by_state(state: str)->Dict[str, Any]:
    """Queries backend db to return results by state

    Args:
        state (str): the state to filter by

    Returns:
        Dict[str, Any]: the results
    """
    results = PJMProjectsModel.query.filter(
        func.lower(PJMProjectsModel.state) == state.lower()
    ).all()

    return dict_helper(results)
     
def projects_by_county_state(county: str, state: str)->Dict[str, Any]:
    """Queries backend db to return results by county and state

    Args:
        county (str): the county to filter by
        state (str): the state to filter by

    Returns:
        Dict[str, Any]: the results
    """
    
    results =  PJMProjectsModel.query.filter(
        func.lower(PJMProjectsModel.state) == state.lower(),
        func.lower(PJMProjectsModel.county) == county.lower()
    ).all()
    return dict_helper(results)