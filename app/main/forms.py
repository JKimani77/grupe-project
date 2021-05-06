from wtforms import SubmitField,TextAreaField, SelectField,StringField, ValidationError
from ..models import User, Post, Review
from flask_wtf import FlaskForm
from wtforms.validators import Required, DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    image = ('upload an image')
    post_info= TextAreaField('post here', validators=[Required()])
    submit = SubmitField('Post')

class ReviewForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')

class SearchForm(FlaskForm):
    search = StringField('')


