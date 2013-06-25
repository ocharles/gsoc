from sqlalchemy.dialects.postgresql import UUID
from app import db

class Review(db.Model):

    __tablename__ = 'reviews'
    __table_args__ = (
            db.Index('reviews_entity_idx', 'entity_class', 'entity_uuid'),)
    id = db.Column(UUID, primary_key=True, 
                   server_default=db.text("uuid_generate_v4()"))
    entity_class = db.Column(db.Enum('release-group', 
                             name='entity_class_enum'))
    entity_uuid = db.Column(UUID, nullable=False)
    author = db.Column(UUID, db.ForeignKey('users.id'), nullable=False)
    text = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    date_last_edit = db.Column(db.DateTime)
    edit_count = db.Column(db.Integer, nullable=False, default=0)
    votes = db.relationship("Vote")
    reports = db.relationship("Report")
