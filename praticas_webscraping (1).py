#!/usr/bin/env python
# coding: utf-8

# In[45]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)


# AO CRIAR UM OBJETO BEAUTIFULSOUP, DOIS ARGUMENTOS SÃO PASSADOS: BS = BEAUTIFULSOUP(HTML.READ(), 'HTML.PARSER')
# O PRIMEIRO É O TEXTO HTML NO QUAL O OBJETO SE BASEIA, E O SEGUNDO ESPECIFICA O PARSER QUE QUEREMOS QUE O BEAUTIFULSOUP USE PARA CRIAR ESSE OBJETO. NA MAIORIA DOS CASOS, O PARSER ESCOLHIDO NÃO FARÁ DIFERENÇA.

# In[46]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)


# CONECTANDO-SE DE FORMA CONFIÁVEL E TRATANDO EXCEÇÕES

# In[47]:


from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')


# NA VERIFICAÇÃO E O TRATAMENTO DE CADA ERRO PARECEM MUITO TRABALHOSO À PRIMEIRA VISTA, MAS É DÁCIL FAZER UMA PEQUENA REORGANIZAÇÃO NESSE CÓDIGO, DEIXANDO-O MENOS DIFÍCIL DE SER ESCRITO (E, ACIMA DE TUDO, MUITO MENO DIFÍCIL DE LER). O CÓDIGO A SEGUIR, POR EXEMPLO, É O MESMO SCRAPER ESCRITO DE MODO UM POUCO DIFERENTE

# In[48]:


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title
    title = getTitle('http://www.pythonscraping.com/pages/warandpeace.html')
    if title == None:
        print('Title could not ne found')
    else:
        print(title)


# In[33]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.findAll('span',{'class':'green'})
for name in nameList:
    print(name.get_text())


# In[39]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.findAll('span',{'class':'green'})
nameList_1 = bs.findAll(text='the prince')

for name in nameList:
    print(name.get_text())
for name in nameList_1:
    print(name.get_text())


# In[41]:


bs.find_all(class_= 'green')


# In[44]:


bs.find_all('The prince',{'class':'green'})


# In[50]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table',{'id':'giftList'}).children:
    print(child)


# In[ ]:




