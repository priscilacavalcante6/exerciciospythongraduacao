#from urllib.request import urlopen
#html = urlopen('https://pythonscraping.com/pages/page1.html')
#print(html.read())

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)