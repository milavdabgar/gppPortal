# app/admin.py
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .extentions import db
from app.modules.user.models import User, Role
from .models import StudyResource
from app.modules.faculty.models import Faculty
from app.modules.student.models import Student


# class BaseAdminView(ModelView):
# from app.modules.module1.views import MyModel1View
# from app.modules.module2.views import MyModel2View
# ... import other module views ...


# from flask_admin.contrib.sqla import ModelView
from flask_security import current_user  # Assuming you're using Flask-Login
from flask import flash

class StudyResourceAdmin(ModelView):

    def create_model(self, form):
        try:
            model = self.model()
            form.populate_obj(model)
            model.creator_id = current_user.id  # Set creator_id to the current user's ID
            self.session.add(model)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash('Failed to create record. ' + str(ex), 'error')
                # log.exception('Failed to create record.')
            self.session.rollback()

            return False
        else:
            self.after_model_change(form, model, True)

        return model



def setup_admin(app):
    # admin = Admin(app, name='GPP Admin', template_mode='bootstrap3')
    admin = Admin(app, name='GPP FlaskAdmin', template_mode='bootstrap3', url='/flask-admin', endpoint='flask-admin')
    
    admin.add_view(ModelView(User, db.session, name='User Admin', endpoint='user_admin', category="Team"))
    admin.add_view(ModelView(Role, db.session, category="Team"))
    admin.add_views(ModelView(Faculty, db.session, category="Team"))
    admin.add_views(ModelView(Student, db.session, category="Team"))
    admin.add_view(StudyResourceAdmin(StudyResource, db.session))
    
    return admin
