from sqlalchemy.dialects.postgresql import UUID
from app import db

class Report(db.Model):

    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(UUID, db.ForeignKey('reviews.id'), nullable=False)
    user = db.Column(UUID, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.Enum('spam', name='report_type_enum'), nullable=False)
