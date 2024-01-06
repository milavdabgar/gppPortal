from flask import render_template, flash, redirect, url_for, request
from flask_security import current_user
from flask_security import auth_required, roles_required, login_required
from app.models import db
from app.main.forms import EditUserForm
from app.main import bp
from app import datastore

@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
# @login_required
def index():
    if "admin" in current_user.roles:
        return redirect(url_for("main.admin"))
    return render_template("main/index.html")

@bp.route('/admin')
# @auth_required("token")
@roles_required("admin")
def admin():
    return render_template("main/admin.html")


@bp.route('/edit_user', methods=['GET', 'POST'])
@login_required
def edit_user():
    form = EditUserForm(obj=current_user)

    if form.validate_on_submit():
        form.populate_obj(current_user)
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for('main.index'))

    return render_template('main/edit_user.html', form=form)

