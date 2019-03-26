import pdfkit
url=raw_input("Enter the URL : ")
filename =  raw_input("Enter the filename : ")
pdfkit.from_url(url,filename+'.pdf')
print("File Saved as "+filename+".pdf")
