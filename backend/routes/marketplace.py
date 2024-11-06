from flask import Blueprint, request, jsonify
from services.blockchain_service import initiate_transaction

bp = Blueprint("marketplace", __name__)

@bp.route("/transaction", methods=["POST"])
def new_transaction():
    data = request.json
    tx_status = initiate_transaction(data["buyer_id"], data["seller_id"], data["product_id"], data["quantity"])
    return jsonify({"status": tx_status})
