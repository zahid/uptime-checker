## Changelog

### v1

Input: a single URL (http for now)
Output: a timestamp, the url, the http status code, and the duration of the request

    usage: `python3 basic-worker/src/uri-check-worker.py http://example.com`

### v2

Update to accept the URL as an environment variable. This will help pave the way for running this in containers.

    ```
    # pass the URL as $1
    python3 basic-worker/src/uri-check-worker.py http://wikipedia.org

    # or use environment variables
    URL=https://yahoo.com python3 basic-worker/src/uri-check-worker.py

    # or specify an interval
    INTERVAL=1 URL=https://wikipedia.org python3 basic-worker/src/uri-check-worker.py

### Backlog

Feature - run the uptime check worker locally w/ docker-compose

Feature - run the uptime checker worker on the server w/ docker-compose

