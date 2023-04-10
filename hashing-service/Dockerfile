#FROM python:latest
# we should avoid using :latest when fetching docker images as it can lead to compatibility issues down the line
# it doesn't matter much in this example but in production we should aim for reproducible builds so I've changed it to the latest python 3.11.2 version as v2 is deprecated 

#RUN curl -sL https://github.com/openfaas/faas/releases/download/0.9.14/fwatchdog > /usr/bin/fwatchdog \
#    && chmod +x /usr/bin/fwatchdog
# for our use case I think wget is better than curl as it's more lightweight and doesn't depend on additional libraries so I've opted to use it instead


FROM python:3.11.2-alpine AS builder
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && wget -qO /usr/bin/fwatchdog https://github.com/openfaas/faas/releases/download/0.9.14/fwatchdog \
    && chmod +x /usr/bin/fwatchdog \
    && apk del .build-deps gcc musl-dev

# added multi-stage builds to reduce overhead
FROM python:3.11.2-alpine
RUN pip3 install flask

COPY --from=builder /usr/bin/fwatchdog /usr/bin/fwatchdog
COPY entrypoint.py .

# the only change here is using python3 for the entrypoint script. I've also updated that script to v3
ENV fprocess="python3 entrypoint.py"


# added healthcheck to make sure the app is running correctly
HEALTHCHECK --interval=10s --timeout=5s \
  CMD wget -qO- http://localhost:8080/health || exit 1

ENTRYPOINT ["python3", "entrypoint.py"]

EXPOSE 8080
CMD [ "fwatchdog" ]