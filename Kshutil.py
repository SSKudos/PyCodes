#This code copies files into a
#new directory
import shutil
import os


def file_cop(src, dest):
    src_file = os.listdir(src)
    for file_name in src_file:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)

file_cop(r'C:\Users\CHIJINDU\Desktop\KUDOSCOPY', r'C:\Users\CHIJINDU\Desktop\KUDOS')
