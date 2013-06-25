from sqlalchemy.dialects.postgresql import UUID
from app import db

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(UUID, primary_key=True)
