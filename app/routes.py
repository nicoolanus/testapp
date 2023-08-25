from app import app

@app.route('/')
def index():
    return "¡Bienvenido a mi aplicación Flask en Docker!"
