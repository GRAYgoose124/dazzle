# Base image
FROM dazzle_dizzy_base AS web 

WORKDIR /app
COPY ./images/web/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# In production we want to remove the volumes and instead:
# COPY ./app .

# unlikely to ever change
ENV DJANGO_SETTINGS_MODULE=dazzlesite.settings

#CMD ["gunicorn", "dazzlesite.asgi:application", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]