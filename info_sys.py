import os
import platform
import psutil
from pprint import pprint


print(platform.uname())
print(psutil.virtual_memory())


pid = os.getpid()
print(pid)
output = os.system(f"cat /proc/{pid}/status")
print(output)


for proc in psutil.process_iter(["pid", "name"]):
    print(proc.info)
    pprint(proc.cmdline())
