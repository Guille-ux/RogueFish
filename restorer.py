import os

with open("host.txt") as f:
  op = f.read()
os.chdir("/etc")
ok = open("hostname", "w")
okw = ok.write(op)
