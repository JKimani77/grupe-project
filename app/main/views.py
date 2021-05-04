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

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        post_info = form.post_info.data
        image = form.image.data
        user_id = current_user
        new_post_object = Post(post_info=post_info,user_id=current_user._get_current_object().id,image=image,title=title)
        new_post_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('new_post.html', form = form)

