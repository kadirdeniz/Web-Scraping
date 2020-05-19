# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:53:24 2020

@author: deniz
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

place=[]
name=[]
year=[]
runtime=[]
genre=[]
rating=[]
desc=[]

apendix='https://www.imdb.com'
veriler=requests.get('https://www.imdb.com/search/title/?groups=top_250&sort=user_rating')
veriler=veriler.content
soup=BeautifulSoup(veriler,'lxml')
first_page='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating'
links=[first_page]
for k in range(4):
    link=apendix+soup.find("a",class_="lister-page-next next-page").get('href')
    links.append(link)
    veriler=requests.get(link)
    veriler=veriler.content
    soup=BeautifulSoup(veriler,'lxml')

for j in links:    
    veriler=requests.get(j)
    veriler=veriler.content
    soup=BeautifulSoup(veriler,'lxml')
    movies=soup.find("div",class_="lister-list")
    each=movies.find_all("div",class_="lister-item-content")
    for i in each:
        place.append(i.h3.span.text)
        name.append(i.h3.a.text)
        year.append(i.find("span",class_="lister-item-year").text)
        runtime.append(i.find("span",class_="runtime").text)
        genre.append(i.find("span",class_="genre").text)    
        rating.append(i.find("div",class_="inline-block ratings-imdb-rating").text)    
        desc.append(i.find("p",class_="text-muted").text)
    
place=pd.DataFrame(place,columns=['place'])
name=pd.DataFrame(name,columns=['name'])
year=pd.DataFrame(year,columns=['year'])
runtime=pd.DataFrame(runtime,columns=['runtime'])
genre=pd.DataFrame(genre,columns=['genre'])
rating=pd.DataFrame(rating,columns=['rating'])  
movies=pd.concat([place,name,year,runtime,genre,rating],axis=1)
movies.to_csv('IMDB.csv')



