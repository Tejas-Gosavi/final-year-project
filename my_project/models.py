from my_project import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    contact_no = db.Column(db.String(10), nullable=True) 
    email = db.Column(db.String(20), unique=True, nullable=True)
    pwd = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<Email %r>' % self.email