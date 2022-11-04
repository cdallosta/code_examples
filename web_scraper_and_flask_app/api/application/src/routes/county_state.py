import logging

from flask import Blueprint, abort, jsonify, make_response, request
from src.controller.county_state import (projects_by_county,
                                         projects_by_county_state,
                                         projects_by_state)

pjm_data_app = Blueprint("pjm_data_app", __name__)
path_prefix = "/pjm_projects"
logger=logging.getLogger(__name__)

@pjm_data_app.app_errorhandler(405)
def method_not_allowed(e):
    """Handles 405 errors
    """
    if request.path.startswith(path_prefix):
        logger.info(e)
        return make_response(jsonify(message="Method Not Allowed"), 405)


@pjm_data_app.app_errorhandler(404)

def invalid_url(e):
    """Handles 404 errors
    """
    logger.info(e)
    return make_response(jsonify(message="Invalid request URL"), 404)


@pjm_data_app.app_errorhandler(Exception)
def internal_server_error(e):
    """Error catch all
    """
    logger.error(e)
    return make_response(jsonify(message="Internal Server Error"), 500)


@pjm_data_app.route(path_prefix, methods=["GET"])
def get_pjm_project_data():
    """
    Parses the request url parameters. Calls the desired callable
    based on the present url parameters. Returns non 200 code when request
    is invalid or if errors occurs during processing

    Returns:
        json: the response object
    """
    county = request.args.get("county")
    state = request.args.get("state")
    arg_keys = list(request.args.keys())
    if not ("county" in arg_keys) and not ("state" in arg_keys):
        
        message = "Invalid request parameters. Valid parameters are 'county' and 'state"
        logger.info(message)
        return abort(
            make_response(
                jsonify(
                    message,
                ),
                400,
            )
        )
    if county and state:
        return make_response(jsonify(projects_by_county_state(county, state)), 200)
    elif county and not state:
        return make_response(jsonify(projects_by_county(county)), 200)
    elif state and not county:
        return make_response(jsonify(projects_by_state(state)), 200)
