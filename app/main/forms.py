from wtforms import SubmitField,TextAreaField, SelectField, ValidationError, StringField
from ..models import User, Post, Review
from flask_wtf import FlaskForm
from wtforms.validators import Required




class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    #image field later

    post_info= TextAreaField('post here', validators=[Required()])
    submit = SubmitField('Post')

class ReviewForm(FlaskForm):
    vote = SelectField(u'vote', choices = [('One-star', '1-Star'),('Two-star', '2 Stars'),('Two-stars', '2-Stars'),('Three-stars', '3-Stars'),('Four-stars', '4-Stars'),('Five-stars', '5-Stars')])
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')



