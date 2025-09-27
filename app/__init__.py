from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SUPABASE_DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Register routes
    from app.routes import register_blueprints
    register_blueprints(app)

    # Simple sanity check route
    @app.route("/")
    def home():
        return {"message": "Backend is running!"}
    
    with app.app_context():
        db.create_all()

    return app
