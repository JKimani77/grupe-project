from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(225))
    email = db.Column(db.String(255),unique=True)
    pass_secure = db.Column(db.String(255))
    pass_hash = db.Column(db.String(255))
    profile_pic = db.Column(db.String())
    post = db.relationship('Post',backref = 'user',lazy='dynamic')
    review = db.relationship('Review', backref = 'user', lazy= 'dynamic')

    @login_manager.user_loader #gets that user with that id when database queries it
    def load_user(user_id):
        return User.query.get(int(user_id))

    @property #make password write-only
    def password(self):
        raise AttributeError('You cant read password attribute')
    
    @password.setter #create password hash
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

     #check if hash has bin stored   
    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)
    
    #for debugging
    def __repr__(self):
        return f'User {self.name}'


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    image = db.Column(db.String())
    post_info = db.Column(db.String(550))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    review = db.relationship('Review', backref = 'post', lazy= 'dynamic')

    def save_post(self):
        db.session.add(self)
        db.session.commit()
        

    def get_post_by_id(cls, id):
        allposts = Post.query.filter_by(id = id).all()
        return allposts


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key = True)
    thoughts = db.Column(db.String(255))
    comments = db.Column(db.String())
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def save_review(self):
        db.session.add(self)
        db.session.commit()
    