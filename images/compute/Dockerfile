ARG COMPUTE_EXTRA_BASE=python:3.10
FROM $COMPUTE_EXTRA_BASE

# Copy all init scripts
COPY ./init_scripts /init_scripts

# Transform the COMPUTE_EXTRA_BASE to a script-friendly format and attempt to run the corresponding init script
RUN SCRIPT_NAME=$(echo $COMPUTE_EXTRA_BASE | cut -d':' -f1 | tr '/' '_').sh && \
    if [ -f "/init_scripts/$SCRIPT_NAME" ]; then \
        bash "/init_scripts/$SCRIPT_NAME"; \
    fi


# Clean up the init scripts to reduce image size
RUN rm -rf /init_scripts/

FROM python:3.10

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV DIZZY_DATA_ROOT="/data/.dizzy"

CMD [ "python", "dizzy_server.py"]
