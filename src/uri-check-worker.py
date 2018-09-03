#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sched
import sys
import time

from util import uri_check_job


# Main program loop
# Schedules the URI check job
def main():
    """ Main program """
    if len(sys.argv) < 2 or sys.argv[1] == "":
        print("usage: main.py URI")
        print("       uri-check-worker.py http://www.yahoo.com")
        exit(1)

    target_uri = sys.argv[1];

    interval = 1  # seconds

    scheduler = sched.scheduler(time.time, time.sleep)

    job = uri_check_job

    scheduler.enter(interval, 1, job, argument=(target_uri,))
    print("Scheduling uri-check-worker for {} at {} check per/sec".format(target_uri, interval))
    while True:
        scheduler.run()
        time.sleep(1)
        scheduler.enter(interval, 1, job, argument=(target_uri,))


if __name__ == "__main__":
    main()