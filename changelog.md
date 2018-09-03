## uri-check-worker

v1 - sat aug 25 2018

Input: a single URL and an expected status code
    - URL must be reachable via http
    - Expected to return an http 200
    - Runs every 5 seconds
    - Outputs CSV-friendly format

Output: a timestamp, the url, and the http status code if successful or -1

v2 - make it into a worker

v3 - make it return some http stats.
    - return time it took for the request to complete

v4 - make it be able to test postgres db connection

v4 - make it possible to test any socket connection

v5 - Write results to db
    - Could be made faster in future by only writing to queue and have some one else write to db?

## GUI

v1- - create a horizontal bar chart showing success fail for a URI over time (per second/minute)

v2 - create some running stats


## Ops

v1 - deploy to something to run
v2 - make invokable via cli


## Other

Tests