def enumerate_list(listas):
	li=[]
	for index, lista in enumerate(listas):
		li.append(f"{index}. {lista}")
	return li

def enumerate_backwards(listas):
	li=[]
	for index, lista in enumerate(listas):
		li.append(f"{index}. {lista[::-1]}")
	return li
