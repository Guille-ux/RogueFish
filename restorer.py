import os

with open("host.txt") as f:
  op = f.read()
  os.system("sudo hostname {}".format(op))
