#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sched
import sys
import time
import os

from util import uri_check_job


# Main program loop
# Schedules the URI check job
def main():
    """ Main program """

    # Use argv $1 or URL env var
    # the URL ENV var will override $1

    target_uri = os.environ['URL']

    if len(sys.argv) > 1:
        target_uri = sys.argv[1]

    if target_uri is None or target_uri is "":
        print("Missing URL environment variable")
        exit(1)

    # seconds
    interval = int(os.environ.get('INTERVAL', 5))

    scheduler = sched.scheduler(time.time, time.sleep)

    job = uri_check_job

    scheduler.enter(interval, 1, job, argument=(target_uri,))
    print("DEBUG - Checking {} every {} seconds".format(target_uri, interval))
    while True:
        scheduler.run()
        time.sleep(1)
        scheduler.enter(interval, 1, job, argument=(target_uri, ))


if __name__ == "__main__":
    main()
