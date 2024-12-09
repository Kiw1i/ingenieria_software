import unittest
from flask import Flask
from Model.__init__ import create_app, db
from Model.models.Elector import Elector as ElectorClass

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        """ Configuración inicial antes de cada prueba """
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Base de datos en memoria para pruebas
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """ Limpieza después de cada prueba """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        """ Prueba la página de inicio """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Decodificar response.data de bytes a str
        response_data = response.data.decode('utf-8')

        # Ahora puedes buscar la cadena 'Iniciar Sesión' dentro de response_data
        self.assertIn('Iniciar Sesión', response_data)


    def test_register_elector(self):
        """ Prueba el registro de un elector """
        with self.app.app_context():
            response = self.client.post('/registrar_elector', data={
                'correo': 'test@test.com',
                'contrasena': 'password123',
                'nombre': 'Test',
                'apellido': 'User'
            })
            self.assertEqual(response.status_code, 302)  # Redirección esperada
            elector = ElectorClass.query.filter_by(correo='test@test.com').first()
            self.assertIsNotNone(elector)
            self.assertEqual(elector.nombre, 'Test')

    def test_login(self):
        """ Prueba el inicio de sesión """
        with self.app.app_context():
            # Agrega un elector para la prueba
            elector = ElectorClass(
                id=None,
                correo='test@test.com',
                contrasena='password123',
                nombre='Test',
                apellido='User'
            )
            db.session.add(elector)
            db.session.commit()

            # Intenta iniciar sesión
            response = self.client.post('/', data={
                'correo': 'test@test.com',
                'password': 'password123'
            })
            self.assertEqual(response.status_code, 302)  # Redirección esperada
            self.assertIn(b'Redirecting', response.data)

    def test_eleccion_page(self):
        """ Prueba la página de elecciones """
        response = self.client.get('/eleccion')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Elecciones', response.data)

if __name__ == '__main__':
    unittest.main()
