from flask import Flask, render_template, request, flash, redirect, session, g, Blueprint
from users.models import social_db, social_connect_db, User, Follows, Post
from forms import PostAddForm, UserEditForm
from auth.auth import do_logout

users_bp = Blueprint('users_bp', __name__, template_folder='templates')


CURR_USER_KEY = "curr_user"


@users_bp.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None

@users_bp.route('/users')
def list_users():
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    users = User.query.all()

    return render_template('/users/index.html', users=users)


@users_bp.route('/users/<user_id>')
def show_user_profile(user_id):

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    posts = Post.query.all()

    user = User.query.get_or_404(user_id)

    return render_template('/users/profile.html', posts=posts, user=user)


@users_bp.route('/users/posts', methods=["GET", "POST"])
def show_user_posts():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    form = PostAddForm()

    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            body=form.body.data,
            user_id=g.user.id
        )

        social_db.session.add(post)
        social_db.session.commit()
        return redirect(f"/users/{g.user.id}")

    return render_template('/users/post.html', form=form)


@users_bp.route('/users/<int:user_id>/following')
def show_following(user_id):
    """Show list of people this user is following."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = User.query.get_or_404(user_id)
    return render_template('users/following.html', user=user)


@users_bp.route('/users/<int:user_id>/followers')
def users_followers(user_id):
    """Show list of followers of this user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = User.query.get_or_404(user_id)
    return render_template('users/followers.html', user=user)


@users_bp.route('/users/follow/<int:follow_id>', methods=['POST'])
def add_follow(follow_id):
    """Add a follow for the currently-logged-in user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    followed_user = User.query.get_or_404(follow_id)
    if followed_user != g.user:
        g.user.following.append(followed_user)
        social_db.session.commit()

    return redirect(f"/users/{g.user.id}/following")


@users_bp.route('/users/stop-following/<int:follow_id>', methods=['POST'])
def stop_following(follow_id):
    """Have currently-logged-in-user stop following this user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    followed_user = User.query.get(follow_id)
    g.user.following.remove(followed_user)
    social_db.session.commit()

    return redirect(f"/users/{g.user.id}/following")


@users_bp.route('/users/profile', methods=["GET", "POST"])
def change_username():
    """Update username for current user."""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = g.user
    form = UserEditForm(obj=user)

    if form.validate_on_submit():
        if User.username_authenticate(form.username.data):
            user.username = form.username.data
            social_db.session.commit()

            return redirect(f"/users/{user.id}")

        flash("Username Not Available", "danger")

    return render_template('users/edit.html', form=form, user=user)


@users_bp.route('/users/delete', methods=["POST"])
def delete_user():
    """Delete user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    do_logout()

    social_db.session.delete(g.user)
    social_db.session.commit()

    return redirect("/signup")
