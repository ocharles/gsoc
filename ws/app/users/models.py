from app import db
from sqlalchemy.dialects.postgresql import UUID

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(UUID, primary_key=True, 
                   server_default=db.text("uuid_generate_v4()"))
