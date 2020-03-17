from flask import *
from flaskblog import db,bcrypt,mail
from flaskblog.models import User,Post
from flask_login import login_user,current_user,logout_user,login_required
from flaskblog.posts.forms import postform

posts= Blueprint('posts','__name__')

@posts.route('/post/new',methods=['POST','GET'])
@login_required
def newpost():
    form=postform()
    if form.validate_on_submit():
        post=Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post has been created','success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html',title='New post',form=form,legend='New post')

@posts.route('/post/<int:post_id>')
def post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('post.html',title='post.title',post=post)

@posts.route('/post/<int:post_id>/update',methods=['POST','GET'])
def updatepost(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = postform()
    if form.validate_on_submit():
        post.title=form.title.data
        post.content=form.content.data
        db.session.commit()
        flash("Post updated",'success')
        return redirect(url_for('posts.post',post_id=post_id))
    elif request.method=='GET':
        form.title.data = post.title
        form.content.data=post.content
    return render_template('create_post.html',title='Update post.title',post=post,form=form,legend='Update post')

@posts.route('/post/<int:post_id>/delete',methods=['POST','GET'])
def deletepost(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted','success')
    return redirect(url_for('main.home'))