#This code walks through a file directory and
#sorts it if size is greater than 300mb
import os

path= r'C:\Users\CHIJINDU\Desktop\MOVIES'

for (path, dirs, files)in os.walk(path):
    for fn in files:
        root = os.path.join(path, fn)
        size = int(os.stat(root).st_size/(1024*1024))
        if(size > 300):
            print(fn + ' ' + str(size) + 'mb')
        else:
            pass

