from flask import Blueprint, jsonify

fraud_bp = Blueprint("fraud", __name__)

# Example route to list fraud alerts
@fraud_bp.route("/", methods=["GET"])
def get_fraud_alerts():
    return jsonify({
        "fraud_alerts": [
            {"message": "Fraud alert 1"},   
        ]
    })

# Example route to create a new fraud alert
@fraud_bp.route("/create", methods=["POST"])
def create_fraud_alert():
    return jsonify({"message": "Fraud alert created!"})
