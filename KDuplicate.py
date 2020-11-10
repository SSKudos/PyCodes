#This code duplicates files while copying
#to a new folder
import shutil  
for i in range(100):
    shutil.copy2(r'C:\Users\CHIJINDU\Desktop\KudosPix\KUDOS-E.jpg',
                 r'C:\Users\CHIJINDU\Desktop\KudosPix\KUDOSCOPY\KUDOS-E{}.jpg'.format(i))
