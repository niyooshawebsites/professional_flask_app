from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models.user import User
from flask import render_template


def register_user(username, email, password):

    existing_user = User.query.filter(
        (User.username == username) |
        (User.email == email)
    ).first()

    if existing_user:
        return render_template('register.html', msg='Username or email already exists.')

    hashed_password = generate_password_hash(password)

    user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return user