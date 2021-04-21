import pyttsx3
import PyPDF2

with open(r'C:\Users\CHIJINDU\Desktop\Esther Vilar - The Manipulated Man.pdf', 'rb') as book:
    reader = PyPDF2.PdfFileReader(book)
    audio_reader = pyttsx3.init()
    audio_reader.setProperty('rate', 100)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()

        audio_reader.say(content)
        audio_reader.runAndWait()
