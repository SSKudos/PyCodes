#Sorts through files and removes duplicates
import os

file= set(os.listdir(r'C:\Users\CHIJINDU\Desktop\AfricanJamz'))
file2 = set(os.listdir(r'C:\Users\CHIJINDU\Desktop\Naija Songz'))

file3 = file.intersection(file2)

print(file3)


#'C:\\Users\\CHIJINDU\\AppData\\Local\\Programs\\Python\\Python38-32'
