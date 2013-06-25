from app import db
from sqlalchemy.dialects.postgresql import UUID

class SpamReport(db.Model):

    __tablename__ = 'spam_report'
    review = db.Column(UUID, db.ForeignKey('review.id'), primary_key=True)
    user = db.Column(UUID, db.ForeignKey('user.id'), primary_key=True)
    created = db.Column(db.DateTime, nullable=False)
