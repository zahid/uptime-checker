## Readme

This thing check if an service is running (http only for now).

This runs a job that issues a HTTP GET request to the provided uri and logs out some results.

See the [Change Log](./changelog.md).

Usage:
```
python3 basic-worker/src/uri-check-worker.py URL
```

Example:
```
INTERVAL=1 URL=https://wikipedia.org python3 basic-worker/src/uri-check-worker.py
DEBUG - Checking https://wikipedia.org every 1 seconds
{'uri': 'https://wikipedia.org', 'duration': 0.4529712200164795, 'status_code': 200, 'ts': 1537322146.158635, 'status': True}
...
```
