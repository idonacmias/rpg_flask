class Creature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    hp = db.Column(db.Integer,nullable=False)
    ac = db.Column(db.Integer, nullable=False)  
    atk_mod = db.Column(db.Integer, nullable=False)
    wallet = db.Column(db.Integer)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

