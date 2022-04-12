web: gunicorn -b "0.0.0.0:$PORT" -w 3 Config.wsgi
release: python manage.py migrate