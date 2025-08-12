from ..extensions import db
from ..models.base import BaseModel

class Post(BaseModel):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    is_flagged = db.Column(db.Boolean, default=False)
