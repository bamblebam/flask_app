from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class postform(FlaskForm):
    title=StringField('Title',validators=[DataRequired(),Length(min=3,max=50)])
    content=TextAreaField('Content',validators=[DataRequired(),Length(min=3,max=1500)])
    submit=SubmitField('Post')