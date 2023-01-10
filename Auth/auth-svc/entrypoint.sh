APP_PORT=${SVC_PORT:-8000}
/opt/venv/bin/gunicorn --workers 4 --worker-tmp-dir /dev/shm core.wsgi:application --bind "0.0.0.0:${APP_PORT}"
