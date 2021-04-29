x = 0

with open('Kfile.txt', 'w') as f:
    while True:
        if x == 99999:
            break
        f.write('\n')
        f.write(str('{:05d}'.format(x))) #Generates 5 digits
        print('{:05d}'.format(x))
        x += 1
