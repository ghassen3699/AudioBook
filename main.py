import pyttsx3
import PyPDF2




print('Create the path of file')
filePath = input('----> ')
book = open(filePath, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in pages:
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
