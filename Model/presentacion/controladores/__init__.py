from flask import Flask

app = Flask(__name__)

from controladores.participantes_controller import participantes_bp
from controladores.proceso_electoral_controller import proceso_electoral_bp

app.register_blueprint(participantes_bp)
app.register_blueprint(proceso_electoral_bp)

if __name__ == '__main__':
    app.run(debug=True)
