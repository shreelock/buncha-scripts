# Opens a random .mkv file from the folder where the script is present
# uses gnome-open, python.
import os
import subprocess
from random import randint

def unix_find(pathin):
    return [os.path.join(path, file)
            for (path, dirs, files) in os.walk(pathin)
            for file in files]

pathlist = unix_find('.')[-1000:]
print "Total files in path :", len(pathlist)
corrlist =[]

for path in pathlist:
  if(path.find('.mkv') !=-1):
    corrlist.append(path)

print "Total mkv files :", len(corrlist)
rint = randint(0,len(corrlist))
rfile = corrlist[rint]
print "Random selected file :", rfile
command = "gnome-open \"{}\"".format(rfile)
subprocess.call(command, shell=True)
