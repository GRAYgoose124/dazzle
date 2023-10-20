# Gunicorn configuration file
# https://docs.gunicorn.org/en/stable/configure.html#configuration-file
# https://docs.gunicorn.org/en/stable/settings.html
import multiprocessing
import os

max_requests = 1000
max_requests_jitter = 50

log_file = "-"

workers = int(os.getenv("N_WEBWORKERS", multiprocessing.cpu_count() * 2 + 1))
