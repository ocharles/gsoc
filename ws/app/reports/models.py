from app import db
from sqlalchemy.dialects.postgresql import UUID

class SpamReport(db.Model):

    __tablename__ = 'spam_report'
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), primary_key=True)
    review_id = db.Column(UUID(as_uuid=True), db.ForeignKey('review.id'), primary_key=True)
    created = db.Column(db.DateTime, nullable=False)
    
    user = db.relationship('User', backref=db.backref('spam_reports'))
    review = db.relationship('Review', backref=db.backref('spam_reports'))
