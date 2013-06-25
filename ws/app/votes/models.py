from app import db
from sqlalchemy.dialects.postgresql import UUID

class Vote(db.Model):

    __tablename__ = 'vote'
    review = db.Column(UUID, db.ForeignKey('review.id'), primary_key=True)
    user = db.Column(UUID, db.ForeignKey('user.id'), primary_key=True)
    type = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
