from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# SQLAlchemy allows us to represent the db structure as classes,
# these classes are refered to as "models".
# Eventually we will be moving these "models" over to a separate file,
# but for now we will be making them in the main file b/c the imports
# and dependencies can get weird.

# Each class, or "model", will be its own table in the db.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # We need to create a "One to Many" relationship between Users and Posts.
    # Each user can have many posts, but each post can only have one author

    # First arg names the class that we want this class to have a relationship with.

    # The 'backref' argument is similar to adding a column to posts,
    # what this allows us to do is when we have a post
    # we can use the author attribute to get the user who created the post.

    # The lazy argument defines when SQLAlchemy loads the data from the db.
    # True means SQLAlchemy will load the data as necessary in one go.
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"