#Reads pdf files
import PyPDF2 as p2

pdfile = open(r'C:\Users\CHIJINDU\Desktop\Java EE 7 with GlassFish 4 Application Server.pdf', 'rb')
pdrd = p2.PdfFileReader(pdfile)

x = pdrd.getPage(1)
print(x.extractText(), '\n')

print(pdrd.getDocumentInfo(),'\n')

print(pdrd.getNumPages())
