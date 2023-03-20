bind = "0.0.0.0:8000"

errorlog = '/usr/src/app/log/gunicorn-error.log'
accesslog = '/usr/src/app/log/gunicorn-access.log'
loglevel = 'debug'

workers = 1