from flask import render_template,redirect,url_for,abort,request, flash
from flask_login import login_required,current_user
from . import main
from .. import db
from ..models import User,Post,Review
from .forms import PostForm,ReviewForm

@main.route('/')
def index():
    posts = Post.query.all()
    #posts = get_post_by_id()

    
    return render_template('index.html', posts= posts)



@main.route('/create_new', methods = ['POST','GET'])
@login_required

def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        post_info = form.post_info.data
        #image = form.image.data
        user_id = current_user
        new_post_object = Post(post_info=post_info,title=title,user_id = user_id)
        new_post_object.save_post()

        

        return redirect(url_for('main.index'))
        import pdb; pdb.set_trace()
        
    return render_template('new_post.html', form = form)


@main.route('/create_review', methods = ['POST', 'GET'])
@login_required
def review(post_id):
    form = ReviewForm()
    post = Post.query.get(post_id)
    all_reviews = Review.query.filter_by(post_id = post_id).all()
    if form.validate_on_submit():
        review = form.review.data
        comments= form.comments.data
        user_id = current_user._get_current_object().id
        post_id = form.post_id.data
        new_review = Review(comments = comments,user_id = user_id,post_id = post_id ,review = review)
        new_review.save_review()
        return redirect(url_for('main.index', post_id = post_id))

    return render_template('review.html', form =form, post = post,all_reviews=all_reviews)





