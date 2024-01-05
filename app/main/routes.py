from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app.models import db
from app.main.forms import EditProfileForm
from app.main import bp


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
# @login_required
def index():
    return render_template("main/index.html")


@bp.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        for attribute in form:
            if attribute.name != 'submit' and attribute.name != 'csrf_token':
                setattr(current_user, attribute.name, attribute.data)
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("main.edit_profile"))
    elif request.method == "GET":
        for attribute in form:
            if attribute.name != 'submit' and attribute.name != 'csrf_token':
                attribute.data = getattr(current_user, attribute.name)
    return render_template("main/edit_profile.html", title="Edit Profile", form=form)