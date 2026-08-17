from datetime import datetime
from app.extensions import db

class User(db.Model):
    __tablename__ = "login_details"
    
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(
        db.String(100),
        unique = True,
        nullable = False
    )
    
    email = db.Column(
        db.String(255),
        unique = True,
        nullable = False
    )
    
    password = db.Column(
        db.String(255),
        nullable = False
    )
    
    created_at = db.Column(
        db.DateTime,
        default = datetime.now
    )
    
    def __repr__(self):
        return f"<User {self.username}>"