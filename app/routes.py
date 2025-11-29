from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from app.forms import LoginForm, VehicleForm
from app.models import db, User, Vehicle

main = Blueprint("main", __name__)

@main.route("/")
@login_required
def index():
    return render_template("index.html")

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("main.index"))
    return render_template("login.html", form=form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))

@main.route("/vehicles", methods=["GET", "POST"])
@login_required
def vehicles():
    form = VehicleForm()
    if form.validate_on_submit():
        v = Vehicle(
            plate=form.plate.data,
            brand=form.brand.data,
            model=form.model.data
        )
        db.session.add(v)
        db.session.commit()
        return redirect(url_for("main.vehicles"))

    vehicles = Vehicle.query.all()
    return render_template("vehicles.html", form=form, vehicles=vehicles)
