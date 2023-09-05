# routes.py
from app.routes import bp

@bp.route('/')
def index():
    return "Hello, World!"
