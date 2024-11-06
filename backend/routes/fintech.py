from flask import Blueprint, request, jsonify
from services.fintech_service import process_loan

bp = Blueprint("fintech", __name__)

@bp.route("/loan", methods=["POST"])
def apply_loan():
    data = request.json
    loan_status = process_loan(data["farmer_id"], data["amount"])
    return jsonify({"status": loan_status})
