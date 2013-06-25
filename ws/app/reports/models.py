from app import db
from sqlalchemy.dialects.postgresql import UUID

class Report(db.Model):

    __tablename__ = 'report'
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(UUID, db.ForeignKey('review.id'), nullable=False)
    user = db.Column(UUID, db.ForeignKey('user.id'), nullable=False)
    type = db.Column(db.Enum('spam', name='report_type_enum'), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
