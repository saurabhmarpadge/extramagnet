import requests
import os, sys
from bs4 import BeautifulSoup

tmp_url = 'http://extra.to/search/?search='

query = input('Enter movie name > ')

url = tmp_url + query + '&s_cat=4&pp=10&srt=seeds&order=desc/'

r0 = requests.get(url)

soup = BeautifulSoup(r0.content,"html.parser")

tlz = soup.find_all("tr",{"class":"tlz"})
tlr = soup.find_all("tr",{"class":"tlr"})

if(tlz == [] and tlr == []):
	print ("The Movie \"" + query + "\" is not Available.")

else:

for item in tlz:
	print(item.contents[0].find_all("a", {"title":"Magnet link"})[0].get("href"))	
	print(item.contents[4].text)
	print(item.contents[5].text)
	print(item.contents[6].text)
	print(item.contents[7].find_all("div")[0].get("class")[0])
	print("\n")

for item in tlr:
	print(item.contents[0].find_all("a", {"title":"Magnet link"})[0].get("href"))	
	print(item.contents[4].text)
	print(item.contents[5].text)
	print(item.contents[6].text)
	print(item.contents[7].find_all("div")[0].get("class")[0])
	print("\n")
  
"""
It returns magnet link
Processing is remaining



	best = "the best magnet"

	if(best != ""):
		print('add -p /home/<user>/Downloads/ ' + best)

		hey = input("\n\n Copy the the contect and press enter")

		os.system('deluge -u console')
"""
