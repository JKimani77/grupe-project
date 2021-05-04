from flask import render_template,redirect,url_for,abort,request
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import User,Post,Review
#from .forms import

@main.route('/')
def index():
    posts = Post.query.all()
    
    return render_template('index.html', posts= posts)
    