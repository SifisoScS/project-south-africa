from ..extensions import db
from ..models.base import BaseModel

class HealthArticle(BaseModel):
    __tablename__ = 'health_articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    verified = db.Column(db.Boolean, default=False)
