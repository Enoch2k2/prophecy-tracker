from config import db
from sqlalchemy_serializer import SerializerMixin

class Prophecy(db.Model, SerializerMixin):
    __tablename__ = "prophecies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    fullfilled = db.Column(db.Boolean)

    def __repr__(self):
        print(f'<Prophecy id={self.id} title={self.title}>')