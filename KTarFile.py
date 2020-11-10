#Extract tar files
import tarfile
my_tar = tarfile.open(r'C:\Users\CHIJINDU\Desktop\dlib-19.21.0.tar.gz')
my_tar.extractall(r'C:\Users\CHIJINDU\Desktop\dfol')
my_tar.close()
