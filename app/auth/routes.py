from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import bp
from app.auth.forms import (
    LoginForm,
    RegistrationForm,
)
from app.models import User


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid user_name or password")
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
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
    form = RegistrationForm()
    if form.validate_on_submit():
        # user = User(user_name=form.user_name.data, email=form.email.data)
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            user_name=form.user_name.data,
            email=form.email.data,
            contact=form.contact.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", title="Register", form=form)