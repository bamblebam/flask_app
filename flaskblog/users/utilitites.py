from flask import *
from flaskblog import db,bcrypt,mail
import secrets
import os
from flask_mail import *

def savepicture(form_picture):
    random_hex=secrets.token_hex(8)
    _,f_ext=os.path.split(form_picture.filename)
    picture_fn=random_hex+f_ext
    picture_path=os.path.join(current_app.root_path,'static/profile_pics/'+ picture_fn)
    form_picture.save(picture_path)
    return picture_fn

def send_reset_email(user):
    token=user.get_reset_token()
    msg=Message('Password reset', sender='deviatewings123@gmail.com',recipients=[user.email])
    msg.body=f'''
    To reset password go to {url_for('users.reset_token',token=token,_external=True)}
    '''
    mail.send(msg)