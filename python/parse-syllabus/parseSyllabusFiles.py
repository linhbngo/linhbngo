from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

import os
import sys

#fp = file(sys.argv[2], 'rb')
f = file(sys.argv[2], "w")
for syllabus in os.listdir(sys.argv[1]):
  if syllabus.endswith(".pdf"):
    print(syllabus)
    print(os.path.join(sys.argv[1],syllabus))    
    fp = file(os.path.join(sys.argv[1],syllabus), 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
      interpreter.process_page(page)
    text = retstr.getvalue()
    device.close()
    retstr.close()
    f.write("=================================================================================\n")
    f.write(syllabus + "\n")
    f.write(text)

f.close()
