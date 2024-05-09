ARG COMPUTE_EXTRA_BASE
FROM $COMPUTE_EXTRA_BASE AS builder
FROM python:3.10

COPY --from=builder / /
COPY ./images/compute/extra/init_scripts /init_scripts
RUN echo "COMPUTE_EXTRA_BASE value is: $COMPUTE_EXTRA_BASE"
RUN bash /init_scripts/select.sh $COMPUTE_EXTRA_BASE
RUN rm -rf /init_scripts/

COPY ./dizzy /dizzy
WORKDIR /app
COPY ./images/compute/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV DIZZY_DATA_ROOT="/data/.dizzy"

CMD [ "python", "dizzy_server.py"]
