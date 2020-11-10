#Merges pdf together

from PyPDF2 import PdfFileMerger
import os

path= r'C:\Users\CHIJINDU\Desktop\\Browse Files\\'

p = os.listdir(path)
merger = PdfFileMerger()

for files in p:
    merger.append(path+files)

if not os.path.exists(path+'Compiled Browsed Python Files.pdf'):
    merger.write(path+ 'Compiled Browsed Python Files.pdf')
merger.close()
