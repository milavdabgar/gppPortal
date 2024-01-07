from flask import render_template, flash, redirect, url_for, request, current_app
from flask_security import current_user, login_required

from . import user
from .forms import EditUserForm
from .models import User, db


# Register routes and handlers for the user blueprint
@user.route("/")
def display_users():
    if not current_user.has_role("admin"):
        return "You don't have permission to view this page", 403
    users = User.query.all()
    return render_template("index.html", users=users)


@user.route("/<int:user_id>")
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
        user = User(
            first_name=data["name"],
            middle_name=data["middle_name"],
            last_name=data["last_name"],
            username=data["username"],
            email=data["email"],
            contact=data["contact"],
            gender=data["gender"],
            dob=data["dob"],
            category=data["category"],
            blood_group=data["blood_group"]
            # roles = data["roles"]
        )  # adjust the fields according to your User class
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("users.routes.user_list"))
    return render_template("user_add.html", form=form)


@user.route("/edit/<int:user_id>", methods=["GET", "POST"])
@login_required
# @roles_required('admin')
def edit_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"message": "User not found"}, 404
    form = EditUserForm(request.form, obj=user)
    if request.method == "POST" and form.validate():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("users.routes.user_list"))
    return render_template("user_edit.html", form=form, user=user)


@user.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditUserForm(obj=current_user)

    if form.validate_on_submit():
        form.populate_obj(current_user)
        db.session.commit()
        flash("User updated successfully!", "success")
        return redirect(url_for("main.index"))

    return render_template("edit_profile.html", form=form)


@user.route("/delete/<int:user_id>", methods=["GET", "POST"])
@login_required
# @roles_required('admin')
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"message": "User not found"}, 404
    if request.method == "POST":
        # Delete the user from the database
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("users.routes.user_list"))
    return render_template("user_delete.html", user=user)
