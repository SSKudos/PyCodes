import zipfile
with zipfile.ZipFile(r'C:\Users\CHIJINDU\Desktop\dlib-19.21.0.tar.gz', 'r') as my_zip:
    print(my_zip.namelist())
    my_zip.extractall(r'C:\Users\CHIJINDU\Desktop\Zfiles')
    
