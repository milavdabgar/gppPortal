from flask import redirect, render_template, flash, url_for
from app import datastore
from app.main.routes import admin
from app.models import db
from app.auth import bp
from flask_security import (
    current_user,
    logout_user,
    login_user,
    hash_password,
    login_required,
    ForgotPasswordForm,
    ChangePasswordForm,
)

# from flask_security.forms import LoginForm, RegisterForm
from app.auth.forms import ExtendedLoginForm, ExtendedRegisterForm
from flask_security.recoverable import (
    send_reset_password_instructions,
    generate_reset_password_token,
    update_password,
)


@bp.route("/login", methods=["GET", "POST"])
# @login_required
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = ExtendedLoginForm()
    if form.validate_on_submit():
        user = datastore.find_user(email=form.email.data)
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("security.login"))
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
    form = ExtendedRegisterForm()
    if form.validate_on_submit():
        if not datastore.find_user(email=form.email.data):
            datastore.create_user(
                email=form.email.data,
                password=hash_password(form.password.data),
                username=form.username.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                contact=form.contact.data,
            )
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("security.login"))
    return render_template("auth/register.html", title="Register", form=form)


@bp.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = datastore.find_user(email=form.email.data)
        send_reset_password_instructions(user)
        flash("Password reset instructions have been sent to your email")
    return render_template(
        "auth/reset_password.html", title="Reset Password", form=form
    )