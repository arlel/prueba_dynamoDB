from chalice import Blueprint, Response
from ..dependencies import user_bl

user_module_blueprint = Blueprint(__name__)


@user_module_blueprint.route("/", methods=["GET"])
def get_all_users():
    users = user_bl.get_users()
    return {"users": users}


@user_module_blueprint.route("/{key}", methods=["GET"])
def get_user_by_key(key: int):
    user = user_bl.get_user(int(key))
    return {"user": user}
