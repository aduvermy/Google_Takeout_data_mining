import re
import time
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import locale
from datetime import datetime
import icu  # PyICU
import pytz # $ pip install pytz


locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

# Fetch the html file
html_doc = googleData = open("./MonActivité.html", encoding='utf8')


# Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

rows = soup.find_all("div", class_="outer-cell")
i = 0
j = 0

searchMonth = []
searchDay = []
searchYear = []
Recherche = []
URL= []

Month = {
          'Jan':1,
          'Feb':2,
          'Mar':3,
          'Apr':4,
          'May':5,
          'Jun':6,
          'Jul':7,
          'Aug':8,
          'Sep':9,
          'Oct':10,
          'Nov':11,
          'Dec':12
          }

for row in rows: 

	i += 1
	print(f"Ligne {i} : ")

	cells = row.find_all("div", class_="content-cell")

	print(cells)

	# search / visited

	substring = "Vous avez consulté"

	if substring in str(cells[0]):

		print("Search")

	# SERP 
		print(cells[0])
		for a in cells[0].find_all('a', href=True):
			
			print(f"SERP : {a['href']}")#récupère le contenu de l'attribut href qui contient l'url du site consulté

			URL.append(a['href'])

			print("\n")

			print(f"KW : {a.string}")#récupère le contenu texte de la balise a => titre de la page consultée

			Recherche.append(a.string)

			

		# Time
		query_time = ''.join(cells[0].find('br').next_siblings)
		print(query_time)

		# Removing timezone
		query_time = query_time.replace(" CET", "")
		query_time = query_time.replace(" à", "")
		print(query_time)


		print(">>" + query_time + "<<")



		query_time=query_time.split(' ')
		print(query_time)

		searchDay.append(query_time[0])
		searchMonth.append(query_time[1])
		print(query_time[0])
		searchYear.append(query_time[2])

		print(query_time)
		print("\n")
		print(f"Date : {query_time}") 
		print("\n")
	
	else:
		print("Visited")

searchDict = {
		'URL':URL,
		'Recherche':Recherche,
        'searchDay':searchDay,
        'searchMonth':searchMonth,
        'searchYear':searchYear
        }

print(searchDict)

searchDF = pd.DataFrame(searchDict)

searchDF.to_csv(path_or_buf = 'D_searchData.csv',index=False)
		

