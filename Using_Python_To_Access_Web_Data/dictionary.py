import PyPDF2
import re

file_dict=open('C:/Users/Sahil/Downloads/largedictionary.pdf','rb')
file_Reader=PyPDF2.PdfFileReader(file_dict)

len=file_Reader.numPages
# print(len)

# for i in range(0,len):
#     pageObj=file_Reader.getPage(i)
#     data=pageObj.extractText()
#     print(data)


oldVJ=""
i=0
for i in range(len):
    page = file_Reader.getPage(i).ex 
    oldVJ=loaweVJ
    print(re.findall('access',oldVJ))
file_dict.close()

print(i)