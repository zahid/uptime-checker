#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sched
import sys
import time
from urllib import request


# Sends an HTTP GET request to a URL and returns the response HTTP status code.
# @param url - the url to retrieve
# @returns the http status code in numeric form. Returns -1 if there was an exception
def get_website_status_code(url):
    status_code = None

    try:
        status_code = request.urlopen(url).getcode()
    except:
        status_code = -1
    
    return url, status_code

# Main program loop
def main():
    """ Main program """
    if len(sys.argv) < 2:
        print("usage: main.py URL")
        print("       main.py http://www.yahoo.com")
        return -1

    # TODO: update to accept environment variables
    # TODO: support a list of URLs
    target_url = sys.argv[1]
    interval = 5  # seconds

    scheduler = sched.scheduler(time.time, time.sleep)

    scheduler.enter(interval, 1, job, argument=(target_url,))

    while True:
        scheduler.run();
        time.sleep(1)
        scheduler.enter(interval, 1, job, argument=(target_url,))

# The unit of work
# This gets a website status, then calls handleResults on the result
def job(target_url):

    url, status = get_website_status_code(target_url)

    result = {
        "time": time.time(),
        "url": url,
        "status": status
    }

    handleResult(result)

    return 0


# Print the results of the job
def handleResult(result):
    print("{},{},{}".format(result["time"], result["url"], result["status"]))


if __name__ == "__main__":
    main()
