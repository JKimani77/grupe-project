class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    image = ('upload an image')
    post_info= TextAreaField('post here', validators=[Required()])
    submit = SubmitField('Post')

class ReviewForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')



