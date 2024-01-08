# app.py
import requests
from flask import render_template, redirect, url_for, request
from . import user
from .forms import EditUserForm

@user.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    form = EditUserForm()

    if request.method == 'GET':
        # API URL
        api_url = f'http://localhost:5000/api/users/{user_id}'  # Adjust the port if different

        # Send a request to the API to get current user data
        response = requests.get(api_url)
        if response.status_code == 200:
            user = response.json()
            form.username.data = user.get('username')
            form.email.data = user.get('email')
            form.first_name.data = user.get('first_name')
            # Populate other fields as necessary
            return render_template('edit_profile.html', form=form, user_id=user_id)
        else:
            return 'User not found.'

    elif form.validate_on_submit():
        # Prepare data for the API request
        user_data = {
            'username': form.username.data,
            'email': form.email.data
            # Add other fields as necessary
        }

        # API URL
        # api_url = f'http://localhost:5000/users/edit/{user_id}'  # Adjust the port if different
        api_url = f'http://localhost:5000/api/users/{user_id}'  # Adjust the port if different

        # Send a request to the API
        response = requests.put(api_url, json=user_data)

        # Handle the response
        if response.status_code == 200:
            return redirect(url_for('user.edit_user', user_id=user_id))
        else:
            return 'Failed to update user.'

    return render_template('edit_user.html', form=form, user_id=user_id)
