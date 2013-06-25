from sqlalchemy.dialects.postgresql import UUID
from app import db

class Vote(db.Model):

    __tablename__ = 'votes'
    review = db.Column(UUID, db.ForeignKey('reviews.id'), primary_key=True)
    user = db.Column(UUID, db.ForeignKey('users.id'), primary_key=True)
    type = db.Column(db.Enum('yes','no',name='vote_type_enum'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
