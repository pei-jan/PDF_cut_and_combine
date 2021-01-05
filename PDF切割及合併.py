#!/usr/bin/env python
# coding: utf-8

# # **刪除檔案夾內所有PDF**

# In[13]:


import os
for file in os.listdir():
    if '.pdf' in file or '.PDF' in file:
        os.remove(file)


# # **重新命名資料夾檔名，設定排序**

# In[18]:


import os
for file in os.listdir():
    if '.pdf' in file or '.PDF' in file:
        newname = file.replace('PDF','pdf')
        num = input('輸入此檔案編號用以排序(ex: 1. ):'+newname)
        newname = num + newname
        os.rename(file,newname)


# # **合併檔案夾內所有PDF**

# In[ ]:


import PyPDF2 , os
pdffiles = []
for file in os.listdir():
    if '.pdf' in file:
        pdffiles.append(file)
pdfoutput = open('comb.pdf','wb')
pdfwriter = PyPDF2.PdfFileWriter()
pdffiles.sort()
for file in pdffiles:
    try:
      pdfreader = PyPDF2.PdfFileReader(open(file,'rb'))
      for pagenum in range(pdfreader.numPages):
          pdfwriter.addPage(pdfreader.getPage(pagenum))
    except:
        pass
pdfwriter.write(pdfoutput)
pdfoutput.close()


# # **切割pdf檔(輸入檔名及切割頁數)**

# In[ ]:


from PyPDF2 import PdfFileReader , PdfFileWriter

readf = input('輸入要切割的pdf檔名(不含.pdf)')
readfile = readf + '.pdf'
pdffilereader = PdfFileReader(readfile,strict = False)
pdfpages = pdffilereader.numPages
part = 0
x = 1
split_list = []
while True:
    if part != str(-1):
        part = input('輸入part'+str(x)+'要切割的頁數(ex:2-6，輸入-1結束)')
        split_list.append(part)
        x += 1
    else:
        split_list.pop()
        break
# while True:
#     if sum(split_list) < pdfpages:
#         part = eval(input('輸入part'+str(x)+'要切割的頁數'))
#         split_list.append(part)
#         x += 1
#     else:
#         split_list.pop()
#         split_list.append(pdfpages - sum(split_list))
#         break

pdffilewriter = PdfFileWriter()

# temp = 0
# for p in range(len(split_list)):
#     for index in range(temp ,temp + split_list[p]):
#         pageobj = pdffilereader.getPage(index)
#         pdffilewriter.addPage(pageobj)
#     pdfoutput = open(readf+str(p+1)+'.pdf','wb')
#     pdffilewriter.write(pdfoutput)
#     pdffilewriter = PdfFileWriter()
#     temp += split_list[p]
#     pdfoutput.close()

for p in range(len(split_list)):
    start_end_page = split_list[p].split('-')
    start_end_page.sort()
    start_page = int(start_end_page[0])-1
    end_page = min(int(start_end_page[1]),pdfpages)
    for index in range(start_page ,end_page):
        pageobj = pdffilereader.getPage(index)
        pdffilewriter.addPage(pageobj)
    pdfoutput = open(readf+str(p+1)+'.pdf','wb')
    pdffilewriter.write(pdfoutput)
    pdffilewriter = PdfFileWriter()
    pdfoutput.close()

