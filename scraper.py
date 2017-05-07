import requests
import pandas as pd
from bs4 import BeautifulSoup
from collections import Counter


def scraper(url, tag):
	try:
		r = requests.get(url)
	except:
		print("la URL digitada no es la correcta")
		exit()
	if r.status_code != 200:
		print("la pagina no responde error ", r.status_code)
		exit()
	soup = BeautifulSoup(r.content, "html.parser")
	data_tag  = soup.findAll(tag)
	if not data_tag:
		print("el TAG buscado no existe")
		exit()
	info_concat=""
	dupli_words = {} 
	for item in data_tag:
		info_concat = info_concat + " " + item.text
	split_info_concat = info_concat.split()
	counter_words = Counter(split_info_concat)
	dict_counter_words = dict(counter_words)

	for item in dict_counter_words:
		if dict_counter_words[item]>1:
			dupli_words[item] = dict_counter_words[item]
	print('*'*30)
	print(pd.Series(dupli_words))
	print('*'*30)

if __name__ == "__main__":
	url = input("ingresar URl de la pagina WEB (SIN HTTP://) = ")
	#url = "www.facebook.com"
	http_url = "http://" + url
	#tag = "div"
	tag = input("ingresar TAG de HTML a buscar = ")
	scraper(http_url, tag)
