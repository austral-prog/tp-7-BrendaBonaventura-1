def index_of_by_index(specific, lista, ind):
	lista=lista[ind:]
	for indice, colores in enumerate(lista):
		if colores==specific:
			return indice
		else:
			return -1

def index_of_empty(lista):
	for indice, words in enumerate(lista):
		if words=="":
			return indice
		else:
			return -1

def index_of(specific, lista):
	for indice, colores in enumerate(lista):
		if colores==specific:
			return indice
		else:
			return -1

def put(sti, lista):
	for indice, words in enumerate(lista):
		if words=="":
			words.replace("", sti)
			return indice
		else:
			return -1

def remove(sti, lista):
	for words in lista:
		if sti==words:
			words.replace(sti, "")
			return lista.count(sti)
