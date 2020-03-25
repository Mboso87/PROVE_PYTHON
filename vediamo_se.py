import os
print(os.getcwd())

contenuto="ciao ciao"
path1="D:\\Michele\\MegaSync\\_PROGETTI\\PYTHON\\"
path2="/HOME/MEGA/PcSYnc/_PROGETTI/"
path=path2
file1=open(path+"esempio_file.txt","w")
file1.write(contenuto)
file1.close()
