from flask import Blueprint, jsonify

posts_bp = Blueprint("posts", __name__)

@posts_bp.route("/all", methods=["GET"])
def profile():
    return jsonify({"message": "All posts"})