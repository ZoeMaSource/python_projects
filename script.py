import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_name):
    greeting = "hello, {}".format(who_name)
    return greeting


name = input("Your Name?")
print(greet(name))


#r = requests.get('https://google.com')
# print(r.status_code)
