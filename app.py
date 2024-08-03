from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user
from utils.auth import User
from utils.forms import LoginForm, ContactForm
from utils.models import User as DBUser, ContactMessage
from extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return DBUser.query.get(user_id)

    # Register routes
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = DBUser.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):  # Ensure password is hashed
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password')
        return render_template('login.html', form=form)

    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template('dashboard.html')

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        form = ContactForm()
        if form.validate_on_submit():
            message = ContactMessage(
                name=form.name.data,
                email=form.email.data,
                message=form.message.data
            )
            db.session.add(message)
            db.session.commit()
            flash('Message sent successfully')
            return redirect(url_for('contact'))
        return render_template('contact.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))

