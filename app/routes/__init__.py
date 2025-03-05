from app.routes.users import users_bp
from app.routes.posts import posts_bp
from app.routes.errors import errors_bp
from app import app

app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(posts_bp, url_prefix="/posts")
app.register_blueprint(errors_bp)