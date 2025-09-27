# app/routes/contacts.py
from flask import Blueprint, request, jsonify
from app.models import Contact
from app import db

contacts_bp = Blueprint("contacts", __name__)


@contacts_bp.route("/", methods=["GET"])
def get_contacts():
    return jsonify({"message": "Contacts endpoint is working!"})


