from flask import redirect, render_template, flash, url_for
from app import datastore
from app.models import db
from app.auth import bp
from flask_security import current_user, logout_user, login_user, hash_password, login_required
from flask_security.forms import LoginForm, RegisterForm

@bp.route("/login", methods=["GET", "POST"])
# @login_required
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = datastore.find_user(email=form.email.data)
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember.data)
        return redirect(url_for("main.index"))
    return render_template("auth/login.html", title="Sign In", form=form)

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RegisterForm()
    if form.validate_on_submit():
        if not datastore.find_user(email=form.email.data):
            datastore.create_user(email=form.email.data, password=hash_password(form.password.data))
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", title="Register", form=form)