from flask import render_template, redirect, url_for, request, current_app
from flask_security import login_required

from . import user
from .forms import EditUserForm, EditProfileForm
from .models import User, db


# Register routes and handlers for the user blueprint
@user.route("/")
def display_users():
    # if not current_user.has_role("admin"):
    #     return "You don't have permission to view this page", 403
    users = User.query.all()
    return render_template("user_list.html", users=users)


@user.route("/show/<int:user_id>")
@login_required
def show_user(user_id):
    user = current_app.user_datastore.find_user(id=user_id)
    if user:
        return render_template("user_view.html", user=user)
    return {"message": "User not found"}, 404


@user.route("/add", methods=["GET", "POST"])
@login_required
# @roles_required('admin')
def add_user():
    form = EditUserForm()
    if request.method == "POST" and form.validate_on_submit():
        data = form.data
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user.display_users", user_id=user.id))
    return render_template("user_add.html", form=form)


@user.route("/edit/<int:user_id>", methods=["GET", "POST"])
@login_required
# @roles_required('admin')
def edit_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"message": "User not found"}, 404
    form = EditProfileForm(request.form, obj=user)
    if request.method == "POST" and form.validate():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("user.display_users", user_id=user.id))
    return render_template("user_edit.html", form=form, user=user)

@user.route("/delete/<int:user_id>", methods=["GET", "POST"])
@login_required
# @roles_required('admin')
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("user.display_users", user_id=user.id))
    return render_template("user_delete.html", user=user)