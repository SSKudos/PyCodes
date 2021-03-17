import os

count=0
for root, dirs, files in os.walk(r"C:\Users\CHIJINDU\Desktop"):
	for file in files:
		if file.endswith(".mp3"):
			print(os.path.join(root, file))
			count +=1

print(count)
