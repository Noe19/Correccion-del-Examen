#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument

db_client = MongoClient("localhost")
my_db = db_client.examen_olimpiadas
my_posts = my_db.tokio1
    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))


# In[10]:


response = requests.get("https://resultados.as.com/resultados/juegos_olimpicos/resultados/")
soup = BeautifulSoup(response.content, "lxml")

Course=[]
Provider=[]
Duration=[]
Start_Date=[]
Offered_By=[]
No_Of_Reviews=[]
Rating=[]

'''
 aqui guardamos con el nombre n.py els scrapping de html 
'''

equi =soup.find_all('span',class_='deporte-nombre')


'''
 aqui todo guardamos en una lista 
'''

equipos =list()
for i in equi:
    equipos.append(i.text)
print(equipos)

    
'''
aqui la guardamos en json a mongodb
'''
for i in range(len(equipos)):
  
    a={
       '3.py':equipos[i]}
    
    my_posts.insert_one(a)
    a={}
    
    
print(equipos)


# In[ ]:





# In[ ]:




