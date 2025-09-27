from .contacts import contacts_bp
from .fraud import fraud_bp

def register_blueprints(app):
    app.register_blueprint(contacts_bp, url_prefix="/api/contacts")
    app.register_blueprint(fraud_bp, url_prefix="/api/fraud")
    print("✅ Blueprints registered")
