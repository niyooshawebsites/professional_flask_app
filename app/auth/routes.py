from flask import (Blueprint, render_template, request, redirect, url_for, session)
from werkzeug.security import (generate_password_hash, check_password_hash)
from app.extensions import db
from app.models.user import User
from app.services.auth_service import register_user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# register route
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        
        if not username or not email or not password:
            return render_template('register.html', msg='Please fill out all the details.')
        
        user = register_user(username, email, password)
        session['user_id'] = user.id
        return redirect(url_for('main.dashboard'))
    
    return render_template('register.html')

# login route
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        
        if not email or not password:
            return render_template("login.html", msg="Please enter email and password.")
        
        user = User.query.filter(User.email == email).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('main.dashboard'))
        
        return render_template('login.html', msg='Invalid credentials')
    
    return render_template('login.html')

# logout route
@auth_bp.route("/logout")
def logout():
    session.clear()
    
    return redirect(url_for('main.home'))