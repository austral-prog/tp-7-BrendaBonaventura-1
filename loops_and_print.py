def enumerate_list(listas):
	li=[]
	index=0
	for index, lista in enumerate(listas):
		if lista:
			li.append(f"{index}. {lista}")
			index=index+1
	return li

def enumerate_backwards(listas):
	li=[]
	index=0
	for index, lista in enumerate(listas):
		if lista:
			li.append(f"{index}. {lista[::-1]}")
			index+=1
	return li
