FROM python:3.6-alpine

ADD ./ /src

# This assumes $URL will be set
CMD ["python", "-u", "/src/uri-check-worker.py"]
