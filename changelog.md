## Changelog

### v1

Input: a single URL (http for now)
Output: a timestamp, the url, the http status code, and the duration of the request

    usage: `python3 basic-worker/src/uri-check-worker.py http://example.com`

### v2 - usage arguments

Update to accept the URL as an environment variable. This will help pave the way for running this in containers.

    ```
    # pass the URL as $1
    python3 basic-worker/src/uri-check-worker.py http://wikipedia.org

    # or use environment variables
    URL=https://yahoo.com python3 basic-worker/src/uri-check-worker.py

    # or specify an interval
    INTERVAL=1 URL=https://wikipedia.org python3 basic-worker/src/uri-check-worker.py


### v3 - containers

Can run with docker, or docker-compose now:

    ```
    # using docker-compose up
    # in uptime-checker/basic-worker
    docker-compose up --build

    # or using docker-compose run
    docker-compose build uri-check-worker
    docker-compose run --rm uri-check-worker

    # or using docker
    docker build -t uri-check-worker src/
    docker run --rm -e URL=http://wikipedia.org -e INTERVAL=1 uri-check-worker
    ```


### Backlog

Feature - run the uptime check worker locally w/ docker-compose

Feature - run the uptime checker worker on the server w/ docker-compose

