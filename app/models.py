from app import db

# -------------------------------
# Contact
# -------------------------------
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }

# -------------------------------
# eWaste Entries
# -------------------------------
class EWasteEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    customer = db.Column(db.String(255), nullable=False)
    distributor = db.Column(db.String(255), nullable=False)
    items = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    reward_points = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "createdAt": self.created_at.isoformat(),
            "customer": self.customer,
            "distributor": self.distributor,
            "items": self.items,
            "notes": self.notes,
            "rewardPoints": self.reward_points,
            "weight": self.weight
        }

# -------------------------------
# Fraud Alerts
# -------------------------------
class FraudAlert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alert_type = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    sim_number = db.Column(db.String(50), nullable=False)
    case_numbers = db.Column(db.JSON, default=list, nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "alertType": self.alert_type,
            "createdAt": self.created_at.isoformat(),
            "simNumber": self.sim_number,
            "caseNumbers": self.case_numbers
        }

# -------------------------------
# Fraud Cases
# -------------------------------
class FraudCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_number = db.Column(db.String(50), unique=True, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    blocked_until = db.Column(db.DateTime, nullable=True)
    customer_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ai_comments = db.Column(db.Text, nullable=True)
    priority = db.Column(db.String(50), nullable=False)
    risk_score = db.Column(db.Integer, nullable=False)
    sim_number = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "caseNumber": self.case_number,
            "category": self.category,
            "createdAt": self.created_at.isoformat(),
            "blockedUntil": self.blocked_until.isoformat() if self.blocked_until else None,
            "customerName": self.customer_name,
            "description": self.description,
            "aiComments": self.ai_comments,
            "priority": self.priority,
            "riskScore": self.risk_score,
            "simNumber": self.sim_number,
            "status": self.status
        }

# -------------------------------
# Learning Hub Courses
# -------------------------------
class LearningHubCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assigned_to = db.Column(db.String(255), nullable=False)
    region = db.Column(db.String(255), nullable=False)
    sessions = db.Column(db.JSON, default=list, nullable=True)
    status = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(255), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "assignedTo": self.assigned_to,
            "region": self.region,
            "sessions": self.sessions,
            "status": self.status,
            "title": self.title
        }

# -------------------------------
# Promotions
# -------------------------------
class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=True)
    category = db.Column(db.String(100), nullable=False)
    conversions = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    discount = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    valid_until = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(255), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "active": self.active,
            "category": self.category,
            "conversions": self.conversions,
            "description": self.description,
            "discount": self.discount,
            "startDate": self.start_date.isoformat(),
            "endDate": self.end_date.isoformat(),
            "validUntil": self.valid_until.isoformat(),
            "title": self.title
        }

# -------------------------------
# Sales
# -------------------------------
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    distributor = db.Column(db.String(255), nullable=False)
    product = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "date": self.date.isoformat(),
            "distributor": self.distributor,
            "product": self.product,
            "price": self.price,
            "quantity": self.quantity,
            "total": self.total,
            "status": self.status
        }

# -------------------------------
# Surveys
# -------------------------------
class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    target_audience = db.Column(db.String(255), nullable=False)
    responses = db.Column(db.Integer, default=0)
    status = db.Column(db.String(50), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "description": self.description,
            "createdAt": self.created_at.isoformat(),
            "targetAudience": self.target_audience,
            "responses": self.responses,
            "status": self.status
        }
