from app import db
from sqlalchemy.dialects.postgresql import UUID

class Review(db.Model):

    __tablename__ = 'review'
    id = db.Column(UUID, primary_key=True, 
                   server_default=db.text("uuid_generate_v4()"))
    release_group_id = db.Column(UUID, index=True)
    author = db.Column(UUID, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    last_updated = db.Column(db.DateTime)
    edits = db.Column(db.Integer, nullable=False, default=0)
    votes = db.relationship("Vote")
    reports = db.relationship("Report")
