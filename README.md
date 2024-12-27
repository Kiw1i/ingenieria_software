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
- Framework: Flask
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

Configuración correcta del pipeline de CI/CD para este proyecto.

### Requisitos previos:
Tener un servidor Jenkins configurado y en funcionamiento.
- Git debe estar instalado y configurado en el entorno de desarrollo.
- SonarQube debe estar instalado y configurado para analizar el código.
- Selenium debe estar configurado para la ejecución de pruebas de funcionalidad.
- OWASP ZAP debe estar disponible para el análisis de seguridad.

#### 1. *Clonación del repositorio*
   Clona el repositorio de tu proyecto en el servidor o entorno donde ejecutarás el pipeline.

   bash
   git clone  https://github.com/Kiw1i/ingenieria_software/
   
#### 2. Configuración de Jenkins
- Instala el plugin de Jenkins necesario para interactuar con Git.
- Instala plugins para SonarQube, Selenium, Pytest y JUnit.
- Crea un nuevo Job en Jenkins para este proyecto.
- Configura el Job para que se ejecute automáticamente cuando se realicen cambios en el repositorio Git.
- Asegúrate de que Jenkins tiene acceso a todas las herramientas necesarias (Selenium, JMeter, ZAP, etc.).
### 3. Configuración de SonarQube
Configura SonarQube con un token de autenticación.
   bash
   git clone ingeneria_software sonar-scanner -Dsonar.projectKey=<nombre_del_proyecto> -Dsonar.host.url=url_del_servidor_sonarqube -Dsonar.login=<token>

### 4. Configuración de Selenium
- Configura Selenium WebDriver en el entorno de Jenkins para ejecutar pruebas de funcionalidad.
- Agrega un paso en Jenkins para ejecutar los tests de Selenium.

### 5. Configuración de ZAP para Análisis de Seguridad
Configura OWASP ZAP en el entorno de Jenkins.
Agrega un paso en el pipeline para ejecutar el análisis de seguridad usando ZAP en tu sistema.
### 6. Configuración de las pruebas unitarias con Pytest
Configura Jenkins para ejecutar Pytest en el pipeline:
   bash
   pytest test/ --html=report.html --self-contained-html

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
![pyunit_report](https://github.com/user-attachments/assets/ecd739f3-eb3b-4403-83f7-5911184538d1)
