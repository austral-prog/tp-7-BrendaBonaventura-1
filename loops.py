def index_of(specific, lista):
	for indice, colores in enumerate(lista):
		if colores==specific:
			return indice
	return -1


def index_of_by_index(specific, lista, ind):
	for indice in range(ind, len(lista)):
		if lista[indice]==specific:
			return indice
	return -1

def index_of_empty(lista):
	for indice, words in enumerate(lista):
		if words=="":
			return indice
	return -1

def put(sti, lista):
	for indice, words in enumerate(lista):
		if words=="":
			lista[indice]=sti
			return indice
	return -1

def remove(sti, lista):
	count=0
	for indice, words in enumerate(lista):
		if sti==words:
			lista[indice]=""
			count+=1
	return count
