Proyecto Final – Bootcamp Testing Automatizado
📌 Descripción

Este proyecto implementa un framework de pruebas automatizadas para validar la funcionalidad de una aplicación Web y su API. El objetivo es cubrir casos de prueba críticos (positivos, negativos y de borde), asegurando calidad, confiabilidad y trazabilidad de los requisitos.

El framework está construido con Python, Pytest, Selenium, Requests y Allure, y se integra con GitHub Actions para ejecutar pruebas de forma continua (CI/CD).

🎯 Objetivos

Diseñar un plan de pruebas completo

Automatizar pruebas funcionales de API y Web UI

Implementar Page Object Model (POM)

Generar reportes automáticos

Integrar pipeline CI/CD

🛠️ Tecnologías

Python, Pytest, Selenium, Requests, Allure, GitHub Actions

📂 Estructura

proyecto-qa-automatizado/
├── README.md
├── requirements.txt
├── tests/
│ ├── api/
│ └── ui/
├── docs/
├── reports/
├── src/
└── .github/
  └── workflows/

🚀 Instalación

Clonar el repositorio:
git clone https://github.com/usuario/proyecto-qa-automatizado.git

cd proyecto-qa-automatizado

Crear y activar entorno virtual:

Windows

python -m venv venv
venv\Scripts\activate

Linux / Mac

python -m venv venv
source venv/bin/activate

Instalar dependencias:
pip install -r requirements.txt

▶️ Ejecución de pruebas

Para correr todos los tests:
pytest -v tests/

Para generar reporte HTML:
pytest --html=reports/report.html

📊 Integración continua (CI/CD)

GitHub Actions ejecuta los tests automáticamente en cada push o pull request y genera reportes de ejecución.
