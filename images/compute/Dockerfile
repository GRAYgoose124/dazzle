ARG COMPUTE_EXTRA_BASE
FROM $COMPUTE_EXTRA_BASE AS builder
FROM dazzle_dizzy_base as compute

COPY --from=builder / /
COPY ./images/compute/extra/init_scripts /init_scripts
RUN echo "COMPUTE_EXTRA_BASE value is: $COMPUTE_EXTRA_BASE"
RUN bash /init_scripts/select.sh $COMPUTE_EXTRA_BASE
RUN rm -rf /init_scripts/

WORKDIR /app
COPY ./images/compute/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

ENV DIZZY_DATA_ROOT="/data/shared/.dizzy"
CMD [ "python", "dizzy_server.py"]
