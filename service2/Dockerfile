#FROM python:latest
# we should avoid using :latest when fetching docker images as it can lead to compatibility issues down the line
# it doesn't matter much in this example but in production we should aim for reproducible builds so I've changed it to the latest python 3.11.2 version as v2 is deprecated 

FROM python:3.11.2

# fwatchdog isn't needed as this service won't recieve any external calls and will only call the other service
#RUN curl -sL https://github.com/openfaas/faas/releases/download/0.9.14/fwatchdog > /usr/bin/fwatchdog \
#   && chmod +x /usr/bin/fwatchdog
#ENV fprocess="python entrypoint.py"

COPY entrypoint.py /entrypoint.py

RUN pip install requests

# added healthcheck to make sure the app is running correctly
HEALTHCHECK --interval=10s --timeout=5s \
  CMD curl --fail http://localhost:8080/health || exit 1

# exposing a port also isn't needed as we won't be recieving calls
#EXPOSE 8080

# since we don't need watchdog, we are instead passing the entrypoint script so it gets executed when the container is started
#CMD [ "fwatchdog" ]

CMD ["python", "/entrypoint.py"]