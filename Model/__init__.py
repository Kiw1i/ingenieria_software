from flask import Flask, render_template, request, redirect, url_for, flash
from Model.extensions import db
from flask_migrate import Migrate
from Model.repositorio.MySQL.elector_repositorio_impl import elector_repositorio_impl
from Model.models.Elector import Elector as ElectorClass
from Model.repositorio.MySQL.candidato_respositorio_impl import candidato_respositorio_impl
from Model.models.Candidato import Candidato as CandidatoClass

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from Model.models import Candidato, Elector, eleccion, registro_electoral, administrador_eleccion
        db.create_all()

    # Aquí se definen las rutas
    @app.route('/')
    def logpage():
        return render_template('login.html')

    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/', methods=['POST'])
    def login():
        correo = request.form['correo']
        contrasena = request.form['password']
        elector = elector_repositorio_impl().obtener_elector_por_correo(correo)

        if elector and elector.contrasena == contrasena:
            print('Inicio de sesión exitoso')
            return redirect(url_for('index'))
        else:
            print('Correo o contraseña incorrectos')
            flash('Correo o contraseña incorrectos', 'error')
            return redirect(url_for('logpage'))

    @app.route('/eleccion')
    def eleccion():
        return render_template('eleccion.html')

    @app.route('/registrar_candidato_view')
    def registrar_candidato_view():
        return render_template('registrar_candidato.html')
    
    @app.route('/registrar_candidato', methods=['POST'])
    def registrar_candidato():
        candidatura = request.form['candidatura']
        partido = request.form['partido']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        candidato = CandidatoClass(
            candidatura=candidatura,
            partido=partido,
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            contrasena=contrasena
        )
        db.session.add(candidato)
        db.session.commit()
        print('Candidato registrado exitosamente')
        return redirect(url_for('registrar_candidato_view'))

    @app.route('/registrar_elector_view')
    def registrar_elector_view():
        return render_template('registrar_elector.html')

    @app.route('/registrar_elector', methods=['POST'])
    def registrar_elector():
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        elector = ElectorClass(
            id=None,
            correo=correo,
            contrasena=contrasena,
            nombre=nombre,
            apellido=apellido
        )
        elector_repo = elector_repositorio_impl()
        if elector_repo.agregar_elector(elector):
            flash('Elector registrado exitosamente', 'success')
        else:
            flash('Error al registrar elector', 'error')
        return redirect(url_for('registrar_elector_view'))

    @app.route('/registro_electoral')
    def registro_electoral():
        return render_template('registro_electoral.html')

    @app.route('/resultados')
    def resultados():
        return render_template('resultados.html')

    @app.route('/modificar_perfil')
    def modificar_perfil():
        return render_template('modificar_perfil.html')

    @app.route('/administrador_eleccion')
    def administrador_eleccion():
        return render_template('administrador_eleccion.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.secret_key = 'supersecretkey'
    app.run(debug=True)
