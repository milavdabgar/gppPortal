from flask import render_template, flash, redirect, url_for, request
from flask_security import current_user, login_required
from app.models import db, User
from app.users.forms import EditUserForm
from app.users import bp


@bp.route("/user_list")
@login_required
def user_list():
    users = User.query.all()
    return render_template("user/user_manage.html", users=users)


@bp.route("/users/<int:user_id>")
@login_required
def show_user(user_id):
    user = User.query.get(user_id)
    if user:
        return render_template("user/user_view.html", user=user)
    return {"message": "User not found"}, 404


@bp.route("/users/add", methods=["GET", "POST"])
@login_required
# @roles_required('admin')
def add_user():
    form = EditUserForm()
    if request.method == "POST" and form.validate_on_submit():
        data = form.data
        user = User(
            first_name = data["name"],
            middle_name = data["middle_name"],
            last_name = data["last_name"],
            username = data["username"],
            email = data["email"],
            contact = data["contact"],
            gender = data["gender"],
            dob = data["dob"],
            category = data["category"],
            blood_group = data["blood_group"]
            # roles = data["roles"]
        )  # adjust the fields according to your User class
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("users.routes.user_list"))
    return render_template("user/user_add.html", form=form)


@bp.route("/users/edit/<int:user_id>", methods=["GET", "POST"])
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
    return render_template("user/user_edit.html", form=form, user=user)


@bp.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditUserForm(obj=current_user)

    if form.validate_on_submit():
        form.populate_obj(current_user)
        db.session.commit()
        flash("User updated successfully!", "success")
        return redirect(url_for("main.index"))

    return render_template("main/edit_profile.html", form=form)


@bp.route("/users/delete/<int:user_id>", methods=["GET", "POST"])
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
    return render_template("user/user_delete.html", user=user)
