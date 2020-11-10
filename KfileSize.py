#Know the size of a file
import os

file_name= r"C:\Users\CHIJINDU\Desktop\THE BLACKLIST 3\The Blacklist.mp4"
file_stats= os.stat(file_name)

print(file_stats)
print(f'File size in Bytes is {file_stats.st_size}')
print(f'File size in Megabytes is {file_stats.st_size/(1024 * 1024)}')
