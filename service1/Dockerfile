#FROM python:latest
# we should avoid using :latest when fetching docker images as it can lead to compatibility issues down the line
# it doesn't matter much in this example but in production we should aim for reproducible builds so I've changed it to the latest python 3.11.2 version as v2 is deprecated 

#RUN curl -sL https://github.com/openfaas/faas/releases/download/0.9.14/fwatchdog > /usr/bin/fwatchdog \
#    && chmod +x /usr/bin/fwatchdog
# for our use case I think wget is better than curl as it's more lightweight and doesn't depend on additional libraries so I've opted to use it instead


FROM python:3.11.2 AS builder
RUN wget -qO /usr/bin/fwatchdog https://github.com/openfaas/faas/releases/download/0.9.14/fwatchdog \
    && chmod +x /usr/bin/fwatchdog

# added multi-stage builds to reduce overhead
FROM python:3.11.2
COPY --from=builder /usr/bin/fwatchdog /usr/bin/fwatchdog

# the only change here is using python3 for the entrypoint script. I've also updated that script to v3
ENV fprocess="python entrypoint.py"
COPY entrypoint.py /

# added healthcheck to make sure the app is running correctly
HEALTHCHECK --interval=10s --timeout=5s \
  CMD curl --fail http://localhost:8080/health || exit 1

EXPOSE 8080
CMD [ "fwatchdog" ]