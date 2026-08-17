from flask import (Blueprint, render_template, session, redirect, url_for)
from app.models.user import User

main_bp = Blueprint("main", __name__)

# home route
@main_bp.route("/")
def home():
    return render_template('index.html')

# dashboard route
@main_bp.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    user = User.query.get(session['user_id'])
    
    if not user:
        session.clear()
        
        return redirect(url_for("auth.login"))
    
    return render_template("dashboard.html",user=user)