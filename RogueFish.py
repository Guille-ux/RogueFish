import os
import sys

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
