from app import db
from app.votes.models import Vote
from utils import compute_rating

from sqlalchemy.dialects.postgresql import UUID
import datetime

class Review(db.Model):

    __tablename__ = 'review'
    
    id = db.Column(UUID(as_uuid=True), server_default=db.text('uuid_generate_v4()'), primary_key=True)
    release_group_id = db.Column(UUID(as_uuid=True), index=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False, server_default=db.text("now()"))
    last_updated = db.Column(db.DateTime, onupdate=datetime.datetime.now)
    edits = db.Column(db.Integer, nullable=False, server_default=db.text("0"))
    rating = db.Column(db.Integer, nullable=False, server_default=db.text("0"))
    
    user = db.relationship('User', backref=db.backref('reviews', lazy='dynamic'))

    def __init__(self, user, text, release_group_id):
        self.user = user
        self.text = text
        self.release_group_id = release_group_id
        
    def update_rating(self):
        """ Compute and update the rank """
        overall = self.votes.count()        
        positive = self.votes.filter(Vote.type != 0).count()
        self.rating = compute_rating(overall, positive)
        return
