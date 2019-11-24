from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placeName = db.Column(db.String(20))
    data = db.Column(db.String(20))
    event = db.Column(db.String(20))
    CoordinatesOnScreen = db.Column(db.String(20))

    def serialize(self):
        return {
            'id': self.id,
            'placename': self.placeName,
            'data': self.data,
            'event':self.event,
            'screenCoords':self.CoordinatesOnScreen

        }