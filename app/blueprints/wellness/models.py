from ..extensions import db
from ..models.base import BaseModel

class SupportResource(BaseModel):
    __tablename__ = 'support_resources'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
