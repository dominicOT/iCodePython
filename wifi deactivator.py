##import subprocess 
##
##wfCMD = subprocess.run (['netsh', 'interface', 'set', 'interface', "wi-fi", "DISABLED"])
##wfCMD


import subprocess 
MyWish = subprocess.run (['netsh', 'interface', 'set', 'interface', "wi-fi", "ENABLED"])
MyWish
