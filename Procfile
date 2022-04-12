web: gunicorn -b "0.0.0.0:$PORT" -w 3 todoapi.wsgi
release: python manage.py migrate