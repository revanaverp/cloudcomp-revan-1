from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Konfigurasi Database (Menggunakan SQLite sebagai database ringan yang terintegrasi)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Contoh Model Database sederhana untuk memenuhi syarat tugas
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return "Halo dari Flask + Database + Docker + Jenkins!"

@app.route('/init-db')
def init_db():
    try:
        # Test query database
        user_count = User.query.count()
        return f"Koneksi Database Berhasil! Jumlah user di DB: {user_count}"
    except Exception as e:
        return f"Gagal terhubung ke database: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
