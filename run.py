from app import app, db

def create_db():
    with app.app_context():
        db.create_all()
        print("Database initialized!")

if __name__ == '__main__':
    create_db()
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))

