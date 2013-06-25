from app import db
from sqlalchemy.dialects.postgresql import UUID

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(UUID, primary_key=True)
