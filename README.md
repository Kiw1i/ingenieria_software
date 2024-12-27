# Pipeline de CI/CD para un sistema de elecciones online
El propósito de este proyecto es automatizar el análisis y evaluación de un proyecto web de sistema de elecciones. Con esto, se pretende facilitar la búsqueda de errores, *code smells*, vulnerabilidades y *bugs*; de este modo evolucionando su desarrollo.

## Índice
1. [Tecnologías](#tecnologías)
   1. [Tecnologías del proyecto web](#tecnologías-del-proyecto-web)
   2. [Tecnologías del pipeline](#tecnologías-del-pipeline)
2. [Instalación y configuración](#instalación-y-configuración)
3. [Secuencia lógica del pipeline](#secuencia-lógica-del-pipeline)
4. [Ejemplos de ejecución](#ejemplos-de-ejecución)

## Tecnologías

Descripción de las tecnologías usadas en la ejecución del proyecto.

### Tecnologías del proyecto web

Sistema de elecciones online
- Lenguaje de programación: Python
- Arquitectura: MVC
- Bibliotecas utilizadas:
  - Flask
  - Flask-Migrate
  - SQLAlchemy
  - mysql-connector-python
  - alembic
  - pytest
  - Flask-SQLAlchemy
  - pytest-flask   
  - pytest-cov     
  - flask-testing

### Tecnologías del pipeline

- Servidor de automatización: Jenkins
  - Sistema de control de versiones: Git
  - Análisis de código fuente: SonarQube
  - Pruebas unitarias: PyUnit
  - Análisis de funcionalidad: Selenium
  - Análisis de rendimiento: Apache JMeter
  - Análisis de seguridad : ZAP

## Instalación y configuración

alguien escriba esto

## Secuencia lógica del pipeline

1. Se clona el repositorio donde se encuentra el sistema de elecciones online (https://github.com/Kiw1i/ingenieria_software).
2. Se configura el entorno virtual y se instalan las dependencias necesarias.
3. Se ejecutan las pruebas unitarias
  - Pruebas para la clase Elector
4. Se realiza el análisis estático del código fuente con SonarQube
5. Se realiza el análisis de seguridad con ZAP
6. Se almacenan los reportes de resultados.

## Reportes de ejecución

Ilustración gráfica del pipeline en Jenkins:
![pipeline](https://github.com/user-attachments/assets/5866094a-c35b-481e-aee1-d0b491e46189)

Reporte de PyUnit:
![sonarqube_report](https://github.com/user-attachments/assets/ecd739f3-eb3b-4403-83f7-5911184538d1)
