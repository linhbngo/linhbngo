import lxml.html, urllib2, urlparse
from urllib2 import Request
from StringIO import StringIO

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter, PDFConverter, LTContainer, LTText, LTTextBox, LTImage
from pdfminer.layout import LAParams

import logging
import sys
import ssl

#logging.basicConfig(
#  format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
#  level=logging.DEBUG
#)

if len(sys.argv) != 3:
  print("Usage: syllabus.py <source url> <directory>")
  exit(-1)

# the url of the page you want to scrape
base_url = sys.argv[1]

# fetch the page
context = ssl._create_unverified_context()
res = urllib2.urlopen(base_url, context=context)

# parse the response into an xml tree
tree = lxml.html.fromstring(res.read())

# construct a namespace dictionary to pass to the xpath() call
# this lets us use regular expressions in the xpath
ns = {'re': 'http://exslt.org/regular-expressions'}

# set up empty list of unique course (not sections)
syllabus = []

# iterate over all <a> tags whose href ends in ".pdf" (case-insensitive)
fileName = sys.argv[2] + "summaryText.txt"
f = open(fileName, "w")
for node in tree.xpath('//a[re:test(@href, "\.pdf$", "i")]', namespaces=ns):
  # print the href, joining it to the base_url
  tmpURL = urlparse.urljoin(base_url, node.attrib['href'])
  #print tmpURL
  openURL = urllib2.urlopen(urllib2.Request(tmpURL), context=context).read()
  memoryFile = StringIO(openURL)
  parser = PDFParser(memoryFile)
  # Create a PDF document object that stores the document structure.
  # Supply the password for initialization.
  document = PDFDocument(parser)
  # Check if the document allows text extraction. If not, abort.
  if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
  # Create a PDF resource manager object that stores shared resources.
  rsrcmgr = PDFResourceManager()
  retstr = StringIO()
  laparams = LAParams()
  codec = 'utf-8'
  # Create a PDF device object.
  device = TextConverter(rsrcmgr, retstr, codec = codec, laparams = laparams)
  # Create a PDF interpreter object.
  interpreter = PDFPageInterpreter(rsrcmgr, device)
  # Process each page contained in the document.
  for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
  memoryFile.close()
  device.close()
  str = retstr.getvalue()
  retstr.close()
  if "data" in str:
#    print node.attrib['href']
    fullSyllabusName = node.attrib['href']
    courseNumber = fullSyllabusName[-19:-15]
    if courseNumber not in syllabus:
      syllabus.append(courseNumber)
      print fullSyllabusName
      print courseNumber
      f.write("=================================================================================\n")
      f.write(fullSyllabusName + "\n")
      f.write(str)
      print tmpURL
  #    print str
f.close()
