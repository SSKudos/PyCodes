#Loop through numbers
x = 0

while True:
	if x == 99999:
		break
	print('{:05d}'.format(x))
	x += 1
