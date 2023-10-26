# Placeholder for base image
ARG COMPUTE_EXTRA_BASE=python:3.10
FROM $COMPUTE_EXTRA_BASE

# If using PyTorch base, then install Triton
RUN if [ "$COMPUTE_EXTRA_BASE" = "pytorch/pytorch" ]; then pip install triton; fi

FROM python:3.10

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV DIZZY_DATA_ROOT="/data/.dizzy"

CMD [ "python", "dizzy_server.py"]
