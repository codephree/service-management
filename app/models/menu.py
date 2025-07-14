from app.extenions import db
from datetime import datetime

class TimestampMixin:
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Profile(db.Model, TimestampMixin):
     id = db.Column(db.Integer, primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     user = db.relationship('User', back_populates='profile')
     

class Request(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(250), nullable=False)
    status = db.Column(db.Integer, default=0)
    resolution_summary = db.Column(db.String(250), nullable=False)
    priority = db.Column(db.String(50), default=True)
    request_by = db.Column(db.Integer)
    assigned_to = db.Column(db.Integer)
    resolved_by = db.Column(db.Integer)

class Incident(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(250), nullable=False)
    status = db.Column(db.Integer, default=0)
    resolution_summary = db.Column(db.String(250), nullable=False)
    priority = db.Column(db.String(50), default=True)
    reported_by = db.Column(db.Integer)
    assigned_to = db.Column(db.Integer)
    resolved_by = db.Column(db.Integer)

class Knowledge(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable= False)
    content = db.Column(db.String(250), nullable= False)
    service_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    
