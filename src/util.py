# These are utility functions
# These should be unit-testable....mostly

import time
from urllib import request,  error


def uri_check_job(uri):
    result = get_uri(uri)
    handle_result(result)


def get_uri(uri):
    try:
        start_time = time.time()
        response = request.urlopen(uri)
        duration = time.time() - start_time
        status = response.getcode()
        info = str(response.info())

    except error.HTTPError as e:
        print("HTTPError", e.code)

        duration = -1
        status = e.code

    return {
        "uri": uri,
        "duration": duration,
        "status": status,
        "timestamp": time.time(),
        "info": info
    }


# Verifies that the result is passing
# Custom logic should be implemented here per scheme
# For now, return True
# @param result - the resultant disctionary from checking a uri
def verify_status(result):
    return True


# handle_result: Handle the result of a check
# @param result - the resultant dictionary from checking a uri
# Prints the result
def handle_result(result):
    print(result)
    print("{},{},{},{}".format(result["timestamp"], result["uri"], result["status"], verify_status(result)))
    return None


