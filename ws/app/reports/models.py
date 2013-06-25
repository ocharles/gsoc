from app import db
from sqlalchemy.dialects.postgresql import UUID

class SpamReport(db.Model):

    __tablename__ = 'spam_report'
    id = db.Column(db.UUID, primary_key=True)
    review = db.Column(UUID, db.ForeignKey('review.id'), nullable=False)
    user = db.Column(UUID, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
