# Base image
FROM python:3.9
WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# In production we want to remove the volumes and instead:
# COPY ./app .

# unlikely to ever change
ENV DJANGO_SETTINGS_MODULE=dazzlesite.settings

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]