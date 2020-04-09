import os
import sys

#Return code: 0 means the service is running; any other code means the service is not running.

status = os.system('systemctl is-active --quiet service-name')
print(status)

#List all processes for all users
service = os.system('ps aux')
print(service)
