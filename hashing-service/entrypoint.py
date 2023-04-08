"""
import sys
import hashlib

inp = sys.stdin.readlines()
hash_func = inp[0].strip()
message = '\n'.join(inp[1:]).strip()

h = hashlib.new(hash_func)
h.update(str.encode(message))

print h.hexdigest()
"""

# the old code is written in Python2 which is deprecated so I've upgraded it to v3 and also made some other
# improvements to make the code more readable and robust it also reads the input from stdin which I've replaced with
# reading from the request from the other service passed by fwatchdog
import hashlib


def handle(req):
    # shorter version of the code which uses .map to avoid loops
    hash_func, *messages = map(str.strip, req.split('\n'))
    message = '\n'.join(messages)

    # added hash validation before creating the hashlib object
    if hash_func not in hashlib.algorithms_guaranteed:
        return "Invalid hash function: {}".format(hash_func)
    else:
        h = hashlib.new(hash_func)
        h.update(message.encode())
        return h.hexdigest()
