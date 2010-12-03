
def ejercicio1(n):
	suma = 0
	for i in range(n):
		suma = suma + (i+1)
	print suma
	
ejercicio1(5)

def ejercicio2(lista):

	for x in lista:
		if x > 3:
			print str(x) + " es mayor que 3"
		else:
			print str(x) + " es menor o igual que 3"
			
lista = [3,4,5,1,8,2,4,9,0]
ejercicio2(lista)