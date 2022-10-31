import json

from chalice import Blueprint, Response
from ..dependencies import user_bl

user_module_blueprint = Blueprint(__name__)


@user_module_blueprint.route("/", methods=["POST"])
def create():
    request = user_module_blueprint.current_request
    # type(request.json_body) -> dict
    user = user_bl.create(request.json_body)
    return {"user": user}


@user_module_blueprint.route("/{key}", methods=["PATCH"])
def update_user_by_key(key: int):
    request = user_module_blueprint.current_request
    user = user_bl.update(request.json_body, int(key))
    return {"user": user}


@user_module_blueprint.route("/", methods=["GET"])
def get_all_users():
    users = user_bl.get_users()
    return {"users": users}


@user_module_blueprint.route("/{key}", methods=["GET"])
def get_user_by_key(key: int):
    user = user_bl.get_user(int(key))
    return {"user": user}


@user_module_blueprint.route("/{key}", methods=["DELETE"])
def delete_user_by_key(key: int):
    user = user_bl.delete(int(key))
    return {"user": user}
