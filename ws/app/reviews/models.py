from app import db
from sqlalchemy.dialects.postgresql import UUID

class Review(db.Model):

    __tablename__ = 'review'
    id = db.Column(UUID, primary_key=True, 
                   server_default=db.text("uuid_generate_v4()"))
    release_group_id = db.Column(UUID, index=True)
    user = db.Column(UUID, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False,
                        server_default=db.text("now()"))
    last_updated = db.Column(db.DateTime, server_default=db.text("null"))
    edits = db.Column(db.Integer, nullable=False,
                      server_default=db.text("0"))
    votes = db.relationship("Vote")
    reports = db.relationship("SpamReport")
