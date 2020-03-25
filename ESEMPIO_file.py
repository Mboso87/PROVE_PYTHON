import os
print(os.getcwd())

contenuto="ciao ciao"
path1="D:\\Michele\\MegaSync\\_PROGETTI\\PYTHON\\"
path2="/HOME/MEGA/PcSYnc/_PROGETTI/PYTHON/"
path=path2
file1=open(path+"esempio_file.txt","w")
file1.write(contenuto)
file1.close()

aggiunta="come va?"
file1=open(path+"esempio_file.txt","a")
file1.write("\n"+aggiunta)
file1.close()

testo=open(path+"esempio_file.txt","r").read()
print(testo)

testo1=open(path+"esempio_file.txt","r").readlines()
testo1

import os
print(os.getcwd())

os.chdir(path+"\\prova_repository")


file1=open("esempio_file1.txt","a")
file1.write("\n"+aggiunta)
file1.close()
