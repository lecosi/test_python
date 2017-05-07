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
	if r.status_code != 200: #prueba de response del servidor de la pag
		print("la pagina no responde error ", r.status_code)
		exit()
	soup = BeautifulSoup(r.content, "html.parser") #mapeo de pag con scraping
	data_tag  = soup.findAll(tag) # busqueda de todos los tags
	if not data_tag: # validacion si la busqueda trae información
		print("el TAG buscado no existe o no tiene información")
		exit()
	info_concat=""
	dupli_words = {}
	for item in data_tag: # concatenación de toda la información de la busqueda
		info_concat = info_concat + " " + item.text
	split_info_concat = info_concat.split() # division de data en un arreglo
	counter_words = Counter(split_info_concat) # utilidad de la libreria colletions para contar las palabras
	dict_counter_words = dict(counter_words) #format a diccionario

	for item in dict_counter_words: # recorrido para saber cuales palabras se repiten y guardarlos en otro diccionario
		if dict_counter_words[item]>1:
			dupli_words[item] = dict_counter_words[item]
	if dupli_words: #validación si existen palabras repetidas
		print('*'*50)
		print(pd.Series(dupli_words)) #usar pandas para mostrar la data con la herramientas SERIES
		print('*'*50)
	else:
		print("en el TAG ", tag, " no se encontraron palabras repetidas!!")
		exit()

if __name__ == "__main__":
	url = input("ingresar URl de la pagina WEB (SIN HTTP://) = ")
	#url = "www.facebook.com"
	http_url = "http://" + url
	#tag = "h1"
	tag = input("ingresar TAG de HTML a buscar = ")
	scraper(http_url, tag)
