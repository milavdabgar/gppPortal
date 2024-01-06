from flask import render_template, flash, redirect, url_for
from flask_security import current_user
from flask_security import login_required
from app.models import db
from app.users.forms import EditUserForm
from app.users import bp

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

