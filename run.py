
from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.create_all()
    if not User.query.filter_by(username='giorgi_2009').first():
        admin = User(username='giorgi_2009',
                     password=generate_password_hash('Giorgi&2009'),
                     is_admin=True)
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
