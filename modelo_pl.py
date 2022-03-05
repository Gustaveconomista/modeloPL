
from selenium import webdriver
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import mysql.connector as mdb

con = mdb.connect(user='root', password ='113283Tt&', database='transfermarkt')

con

cursor = con.cursor()

cursor

html_plm = "https://www.transfermarkt.com.br/premier-league/gesamtspielplan/wettbewerb/GB1?saison_id=20"

def cap_html(x):
    f = html_plm + str(0) + str(x)
    return f

l0 = []
for x in range(0,10):
    l0.append(cap_html(x))

l0

def cap_html1(x):
    f = html_plm + str(x)
    return f

l1 = []
for x in range(10,22):
    l1.append(cap_html1(x))

l1

for x in (l0):
    fields = {}
    driver = webdriver.Chrome()
    driver.get(x)
    h = driver.page_source
    soup = BeautifulSoup(h, 'lxml')
    driver.quit()
    for i in range(0,380):
        fields = {}
        driver = webdriver.Chrome()
        driver.get(x)
        h = driver.page_source
        soup = BeautifulSoup(h, 'lxml')
        driver.quit()
        m = soup.find_all('td', attrs={'class' :  'text-right no-border-rechts hauptlink'})
        r = soup.find_all('td', attrs={'class' :  'zentriert hauptlink'})
        v = soup.find_all('td', attrs={'class' :  'no-border-links hauptlink'})
        mandante = m[i].text
        resultado = r[i].text
        visitante = v[i].text
        fields["Mandante"] = mandante
        fields["Resultado"] = resultado
        fields["Visitante"] = visitante
        for j in range(0,10):
            #insert('transfermarkt', fields)
            insertstrfmkt=("INSERT INTO partidaspl0" + str(j) + " (mandante, resultado, visitante) values ('%s', '%s', '%s')" % (mandante, resultado, visitante))
            cursor.execute(insertstrfmkt)
            #print(insertstmt)
            #print(fields)
            #print ('%s\t,%s\t' % (jogadores,valores))

con.commit()

for x in range(1,10):
    cursor.execute("DROP TABLE partidaspl0"+str(x))

con.commit()

m = []
for i in l:
    m.append(cap_soup(i))

m

len(m[0])

len(mpl_html)

m

len(m)

def cap_soup(x):
    m = soup.find_all('td', attrs={'class' :  'text-right no-border-rechts hauptlink'})
    return m

cap_soup(mpl)

def create_table0(x):
    query1 = "CREATE TABLE partidaspl" + str(0) + str(x) + " (mandante TEXT NOT NULL, resultado TEXT NOT NULL, visitante TEXT NOT NULL)"
    return cursor.execute(query1)

def create_table1(x):
    query1 = "CREATE TABLE partidaspl" + str(x) + " (mandante TEXT NOT NULL, resultado TEXT NOT NULL, visitante TEXT NOT NULL)"
    return cursor.execute(query1)

for x in range(0,10):
    create_table0(x)

for x in range(10,22):
    create_table1(x)

def data_add(x):
    query2 = "INSERT INTO partidaspl" + str(x) + " (mandante, resultado, visitante) values ('%s', '%s', '%s')" % (mandante, resultado, visitante)
    return cursor.execute(query2)

mpl = "https://www.transfermarkt.com.br/premier-league/gesamtspielplan/wettbewerb/GB1/saison_id/2021"

cap_soup(mpl)

mpl

driver = webdriver.Chrome()

driver.get(mpl)

mpl_html = driver.page_source

mpl_html

len(mpl_html)

'Resultado' in mpl_html

mpl_soup = BeautifulSoup(mpl_html, 'lxml')

mpl_soup

m = mpl_soup.find_all('td', attrs={'class' :  'text-right no-border-rechts hauptlink'})

m

len(m)

m[0].text

r = mpl_soup.find_all('td', attrs={'class' :  'zentriert hauptlink'})

r

len(r)

r[0].text

v = mpl_soup.find_all('td', attrs={'class' :  'no-border-links hauptlink'})

v

len(v)

v[0].text

for i in range(0,380):
    fields = {}
    mandante = m[i].text
    resultado = r[i].text
    visitante = v[i].text
    fields["Mandante"] = mandante
    fields["Resultado"] = resultado
    fields["Visitante"] = visitante
    #insert('transfermarkt', fields)
    insertstrfmkt=("INSERT INTO partidaspl2122 (mandante, resultado, visitante) values ('%s', '%s', '%s')" % (mandante, resultado, visitante))
    cursor.execute(insertstrfmkt)
    #print(insertstmt)
    #print(fields)
    #print ('%s\t,%s\t' % (jogadores,valores))

con.commit()

cursor.execute("SELECT * FROM partidaspl2122")

p = cursor.fetchall()

p

def read_table(table):
    query = "SELECT * FROM " + table
    return pd.read_sql(query,con)

partidas_pl2122 = read_table('partidaspl2122')

partidas_pl2122
