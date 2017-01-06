import os, sys
from bs4 import BeautifulSoup

import os
name = input('Enter moive> ')
os.system('phantomjs download.js '+name)

page_name="html_page.html"
local_page = open(page_name,"r")
soup = BeautifulSoup(local_page,"lxml")


tlz = soup.find_all("tr",{"class":"tlz"})
tlr = soup.find_all("tr",{"class":"tlr"})


if(tlz == [] and tlr == []):
	print ("The Movie \"" + name + "\" is not Available.")
else:
	count = 0

	for item in tlz:
		count = count + 1
	for item in tlr:
		count = count + 1

	movie = []
	for i in range(count):
		movie.append([])
	i = 0
	
	for item in tlr:
		movie[i].append(item.contents[0].find_all("a", {"title":"Magnet link"})[0].get("href"))	
		movie[i].append(item.contents[4].text)
		movie[i].append(item.contents[5].text)
		movie[i].append(item.contents[6].text)
		movie[i].append(item.contents[7].find_all("div")[0].get("class")[0])
		i = i + 1

	for item in tlz:
		movie[i].append(item.contents[0].find_all("a", {"title":"Magnet link"})[0].get("href"))	
		movie[i].append(item.contents[4].text)
		movie[i].append(item.contents[5].text)
		movie[i].append(item.contents[6].text)
		movie[i].append(item.contents[7].find_all("div")[0].get("class")[0])
		i = i + 1

	max_possible = -999
	index = -1
	for i in range(count):
		div = int(movie[i][2])/int(movie[i][3])
		if(div>max_possible):
			max_possible = div
			index = i
	best = movie[index][0]
	
	choice = input('Download Using\n1. Aria2\n2. Deluge\n3. Magnet Link\n> ')
	stop = True
	while(stop):
		if(choice=='1'):
			stop = False
			os.system('aria2c '+best)
			print('Download Complete')
		elif(choice=='2'):
			stop = False
			print('add -p /home/<user>/Downloads/ ' + best)
			input("\n\n Copy the the contect and press enter")
			os.system('deluge -u console')
		elif(choice=='3'):
			stop = False			
			print(best)
		else:   
			print('Invalid choice. Try Again!!!')
			choice = input('Download Using\n1. Aria2\n2. Deluge\n3. Magnet Link\n> ')
