# Repositorios del sistema de elecciones online

Fork del [Sistema de elecciones online](https://github.com/Kiw1i/ingenieria_software)

## Descripción

El objetivo del proyecto original es implementar un sistema que permita a los usuarios programar elecciones para la fecha deseada, entre los candidatos inidicados y para los electores a quienes compete. Este fork implementa la parte de los repositorios y conexiones a base de datos del sistema, así como modelos de flujo de información entre las diversas capas.

## Estilos

### Manejo de errores/excepciones: Pasivo-agresivo

El programa busca comunicar claramente el error arrojado que causó su terminación.

```python
try:
    db.session.add(eleccion)
    db.session.commit()
except:
    db.session.rollback()
    raise
finally:
    db.session.close()
```

### Tablas de persistencia

Los datos se almacenan en una base de datos relacional a la que se accede mediante consultas SQL.

Se accede a ellos usando las funciones ORM de la biblioteca SQLAlchemy para Flask.

```python
entrada = db.session.query(AdministradorModelo).filter_by(id = admin_id).one()
admin_nombre = entrada.nombre
```

### Trinity (MVC)

La base de datos se comunica con los repositorios a través de una clase (modelo), que a su vez comunica a los repositorios con el dominio y viceversa.

```python
db.session.add(admin)
```

```python
admin_nombre = entrada.nombre
```

## Uso

Se puede acceder a los repositorios mediante su interfaz, enviando la información pertinente a través de su modelo correspondiente. La información, si existe, se extraerá de la base de datos.

## Autor

Kristopher Rospigliosi Gonzales