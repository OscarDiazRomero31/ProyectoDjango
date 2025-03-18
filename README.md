# ProyectoDjango
Proyecto Servidor Tercer Trimestre

# Pasos en Casa desde un proyecto ya creado por git
Descargar proyecto con GIT
sudo apt-get install python3-venv  -> Sino está instalado ya
No situamos en la carpeta 2daw
python3 -m venv myvenv -> Creamos el entorno
source myvenv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate -> Creamos base de datos
python manage.py runserver 0.0.0.0:8080 -> Lanzamos el servidor

