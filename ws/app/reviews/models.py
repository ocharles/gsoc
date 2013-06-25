from app import db
from sqlalchemy.dialects.postgresql import UUID

class Review(db.Model):

    __tablename__ = 'review'
    __table_args__ = (
            db.Index('review_entity_idx', 'entity_class', 'entity_uuid'),)
    id = db.Column(UUID, primary_key=True, 
                   server_default=db.text("uuid_generate_v4()"))
    entity_class = db.Column(db.Enum('release-group', 
                             name='entity_class_enum'))
    entity_uuid = db.Column(UUID, nullable=False)
    author = db.Column(UUID, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    last_updated = db.Column(db.DateTime)
    edits = db.Column(db.Integer, nullable=False, default=0)
    votes = db.relationship("Vote")
    reports = db.relationship("Report")
