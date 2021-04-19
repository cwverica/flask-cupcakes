from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


"""Models for Cupcake app."""

class Cupcake(db.Model):
    '''Cupcake model itself'''

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String(20), nullable=False)
    size = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(110), nullable=False)

    def serialize_cupcake(self):
        
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }