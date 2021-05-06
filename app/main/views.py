from flask import render_template,redirect,url_for,abort,request
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..request import search_user
from ..models import User,Post,Review
from .forms import PostForm, ReviewForm, SearchForm

@main.route('/')
def index():
    posts = Post.query.all()
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('main.search'))
        
    
    return render_template('index.html', posts= posts)

@main.route('/search', methods = ['POST','GET'])
@login_required
def search():
    '''
    function to return github users search results
    '''
    searched = search_user(username,page)

    return render_template('search.html' searched = searched)





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
        new_post_object.save_post()
        return redirect(url_for('main.index'))
        
    return render_template('new_post.html', form = form)

@main.route('/review', methods = ['POST','GET'])
@login_required
def review(post_id):
  form = ReviewForm()
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

'''
@main.route('/')
def upload_form():
	return render_template('upload.html')

@main.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed below')
		return render_template('upload.html', filename=filename)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@main.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

  '''




