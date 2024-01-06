from flask import render_template, redirect, url_for
from flask_security import current_user
from flask_security import roles_required, login_required
from . import main


@main.route("/", methods=["GET", "POST"])
@main.route("/index", methods=["GET", "POST"])
@login_required
def index():
    if "admin" in current_user.roles:
        return redirect(url_for("main.admin"))
    return render_template("index.html")

@main.route('/admin')
@roles_required("admin")
def admin():
    return render_template("admin.html")