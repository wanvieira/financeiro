from flask import Flask

from config import Config

from models import db

from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.despesas import despesas_bp
from routes.parcelamentos import parcelamentos_bp
from routes.receitas import receitas_bp

app = Flask(__name__)

app.secret_key = 'financeiro123'

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth_bp)

app.register_blueprint(dashboard_bp)

app.register_blueprint(despesas_bp)

app.register_blueprint(parcelamentos_bp)

app.register_blueprint(receitas_bp)

with app.app_context():
    db.create_all()

print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)