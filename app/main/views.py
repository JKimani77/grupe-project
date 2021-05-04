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

def review(post_id):
  form = ReviewForm
  post = Post.query.get(post_id)
  all_reviews = Review.query.filter_by(post_id = post_id).all()
  if form.validate_on_submit():
    thoughts = form.thoughts.data
    comments= form.comments.data
    user_id = current_user._get_current_object().id
    post_id = post_id
    new_review = Review(comments = comments,user_id = user_id,post_id = post_id ,thoughts = thoughts)
    new_review.save_r()
        return redirect(url_for('.review', post_id = post_id)

    return render_template('review.html', form =form, post = post,all_reviews=all_reviews)





