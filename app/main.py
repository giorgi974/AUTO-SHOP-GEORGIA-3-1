from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.forms import CarForm
from app.models import Car, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    cars = Car.query.all()
    return render_template('index.html', cars=cars)

@main.route('/add_car', methods=['GET', 'POST'])
@login_required
def add_car():
    if not current_user.is_admin:
        flash('მხოლოდ ადმინს აქვს მანქანის დამატების უფლება.', 'danger')
        return redirect(url_for('main.index'))

    form = CarForm()
    if form.validate_on_submit():
        new_car = Car(
            image_url=form.image_url.data,
            description=form.description.data,
            price=form.price.data
        )
        db.session.add(new_car)
        db.session.commit()
        flash('მანქანა წარმატებით დაემატა!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_car.html', form=form)
