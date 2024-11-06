from flask import Blueprint, request, jsonify
from services.ai_service import get_crop_health

bp = Blueprint("crop_monitoring", __name__)

@bp.route("/health", methods=["GET"])
def crop_health():
    data = request.args.get("sensor_data")
    health = get_crop_health(data)
    return jsonify({"crop_health": health})
