from extensions import db
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id

    @staticmethod
    def get(user_id):
        return db.session.query(User).filter_by(id=user_id).first()

