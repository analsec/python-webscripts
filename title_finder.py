#/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import sys

def get_title(url): 
	try:
		r = requests.get(url)
		soup = BeautifulSoup(r.text,'html.parser')
		title = soup.find('title')
		print(title.string + " - " + url)
	except:
		print("don't have title - " + url)

def openLinks(archivo):
	with open(archivo,"r") as f:
		lista = f.readlines()
	listaVacia = []
	for link in lista:
		listaVacia.append(link.rstrip())
	return listaVacia


def help():
	print("""usage: python3 """+sys.argv[0]+""" [list|target] [file|url]
  
Title finder

	h/help - Show this help
	l/list - Read file with targets
	t/target - Select one target

	Ex:
		python3 """ + sys.argv[0] + """ l anal.txt
		python3 """ + sys.argv[0] + """ t https://www.analsec.org
""")


if len(sys.argv) > 1:
	opt = sys.argv[1].lower()

	if opt == "help" or opt == "h":
		help()

	elif len(sys.argv) != 3:
		help()
	else:
		if opt == "l" or opt == "list":
			with Pool(150) as p:
				p.map(get_title,openLinks(sys.argv[2]))
				p.close()
				p.join()

		elif opt == "t" or opt == "target":
			get_title(sys.argv[2])

		else:
			help()
else:
	help()
