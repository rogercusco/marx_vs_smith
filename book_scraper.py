##################################################################################
# SCRAPER FOR BOOKS AVAILABLE ONLINE AT econlib.org
##################################################################################

#import required modules

import urllib2
from bs4 import BeautifulSoup as bs 
import os 
import numpy as np
import sys
import json

#### ----scrape Das Kapital----
url = 'http://www.econlib.org/library/YPDBooks/Marx/mrxCpA.html'
parsed = urllib2.urlopen(url).read()

# print parsed
soup = bs(parsed)

# get href for each chapter
chap = []
for link in soup.find_all('a'):  
    raw_link = link.get('href')
    #print type(raw_link)
    if type(raw_link) is str:
        chap.append(raw_link.split("#",1)[0])
    else:
        next

# filter to chapters written by Marx
chaps = chap[21:63]
#print chaps


# build urls for each chapter and scrape their content in paragraphs
capital = ["The Capital", "Karl Marx"]
chapters = []

for chapter in chaps:
    
    paragraphs = []
    url = 'http://www.econlib.org/library/YPDBooks/Marx/'+ chapter 
    body = urllib2.urlopen(url).read()
    soup = bs(body)   
    parags = soup.find_all('p')
    
    for parag in parags:
        paragraphs.append(parag.get_text())
        
    chapters.append(paragraphs)
    
   # if len(chapters) > 3:
   #     break

capital.append(chapters)

#### ----scrape The Wealth of Nations----
url = 'http://www.econlib.org/library/Smith/smWN.html'
parsed = urllib2.urlopen(url).read()

# print parsed
soup = bs(parsed)

# get href for each chapter
chap = []
for link in soup.find_all('a'):  
    raw_link = link.get('href')
    #print type(raw_link)
    if type(raw_link) is str:
        chap.append(raw_link.split("#",1)[0])
    else:
        next
        
#print chaps
# filter to chapters written by Marx

chaps = chap[18:54]

# build urls for each chapter and scrape their content in paragraphs
wealth = ["The Wealth of Nations", "Adam Smith"]
chapters = []

for chapter in chaps:
    
    paragraphs = []
    url = 'http://www.econlib.org/library/Smith/'+ chapter 
    body = urllib2.urlopen(url).read()
    soup = bs(body)   
    parags = soup.find_all('p')
    
    for parag in parags:
        paragraphs.append(parag.get_text())
        
    chapters.append(paragraphs)

wealth.append(chapters)

# create a list to store all the books
bookshelf = [capital, wealth]

# write a json file with the bookshelf of scraped books
with open('bookshelf.json', 'w') as file:
     json.dump(bookshelf, file)