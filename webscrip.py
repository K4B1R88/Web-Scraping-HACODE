import bs4
import requests
import webbrowser
import sys
import os
import time
import pyfiglet
import colorama
from colorama import Fore , Back , Style
colorama.init(autoreset = True)

#color
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'


def logo():
	os.system('clear')
	print('''
▒█░░▒█ █▀▀ █▀▀▄         
▒█▒█▒█ █▀▀ █▀▀▄                   ./HACODE
▒█▄▀▄█ ▀▀▀ ▀▀▀░ 

▒█▀▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀█ ░▀░ █▀▀▄ █▀▀▀ 
░▀▀▀▄▄ █░░ █▄▄▀ █▄▄█ █░░█ ▀█▀ █░░█ █░▀█ 
▒█▄▄▄█ ▀▀▀ ▀░▀▀ ▀░░▀ █▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀▀''')





def first():
	os.system('clear')
	logo()
	print("")
	print(cyan+b+"----------------------------------"+b+cyan)
	print(gren+b+"Author	: HACODE                 |"+b+gren)
	print (red+b+"Team	: UNITED HACKERS         |"+b+red)
	print (yellow+b+"YouTube	: HACODE                 |"+b+yellow)
	print(cyan+b+"----------------------------------"+b+cyan)
	
first()

def common():
	url = input(cyan+b+"Enter Website link for Scraping : "+b+cyan)
	data = requests.get(url)
	soup = bs4.BeautifulSoup(data.text, "html.parser")
	 #print(soup.prettify())
	filename = input(cyan+b+"Enter file name to save file : "+b+cyan)
	mycode = open(filename+".html", "w")
	mycode.write(soup.prettify())
	mycode.close()
	print("Your file is save")
	time.sleep(2)
	print("")



		


	


def gethref(self):
	url = input(cyan+b+"Enter Website link for Scraping : "+b+cyan)
	data = requests.get(url)
	soup = bs4.BeautifulSoup(data.text, "html.parser")
	for links in soup.find_all('a'):
		link = links.get('href')
		if link[0:3] == "../" and link !="#":
			print("Links in website :  " + link[2:len(link)])
		elif link[0] == "/" and link != "#":
			print("Links in website :  " + link)


while True:
	
	os.system('clear')
	logo()
	first()
	print(gren+b+'''
[1] Copy website code
[2] Get all href link in website
[3] Exit
'''+b+gren)
	a = int(input(cyan+b+"SELECT OPTION : "+b+cyan))
	if a == 1:
		common()
	elif a == 2:
		gethref('h')
	elif a== 3:
		exit()




