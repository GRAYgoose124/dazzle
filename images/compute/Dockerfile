ARG USE_GPU=false
FROM ${USE_GPU:+nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04}
FROM python:3.10
WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# In production we want to remove the volumes and instead:
# COPY ./app .

# unlikely to ever change
ENV DIZZY_DATA_ROOT="/data/.dizzy"

CMD [ "python", "dizzy_server.py"]