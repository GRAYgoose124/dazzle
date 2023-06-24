FROM python:3.9
WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# In production we want to remove the volumes and instead:
# COPY ./app .

CMD [ "python", "dizzy_server.py"]