from app.routes import users
from app import app

app.register_blueprint(users.users_bp, url_prefix="/users")