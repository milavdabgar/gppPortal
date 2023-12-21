from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app import db
from app.main.forms import EditProfileForm
from app.main import bp

# from app.routes.cart_routes import get_cart_count


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
# @login_required
def index():
    return render_template("main/index.html")


@bp.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.user_name)
    if form.validate_on_submit():
        current_user.full_name = form.full_name.data
        current_user.user_name = form.user_name.data
        current_user.email = form.email.data
        current_user.contact = form.contact.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("main.edit_profile"))
    elif request.method == "GET":
        form.full_name.data = current_user.full_name
        form.user_name.data = current_user.user_name
        form.email.data = current_user.email
        form.contact.data = current_user.contact
    return render_template("main/edit_profile.html", title="Edit Profile", form=form)
