
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Car
from app.forms import CarForm


main = Blueprint('main', __name__, template_folder='../templates')


@main.route('/')
def home():
    cars = Car.query.all()
    return render_template('home.html', cars=cars)

@main.route('/add_car', methods=['GET', 'POST'])
@login_required
def add_car():
    if not current_user.is_admin:
        flash('Access denied! Only admins can add cars.', 'danger')
        return redirect(url_for('main.home'))

    form = CarForm()
    if form.validate_on_submit():
        new_car = Car(
            image_url=form.image_url.data,
            description=form.description.data,
            price=form.price.data
        )
        db.session.add(new_car)
        db.session.commit()
        flash('Car added successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('add_car.html', form=form)
