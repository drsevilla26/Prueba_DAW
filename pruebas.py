class ClaseBase:
	def metodobase(self):
		print "Metodo Base"

class MiClase(ClaseBase):
	def metodo1(self):
		print "HOLA CLASE"

print "Hola Mundo"

def imprimirelementos(elementos):
	for x in elementos:
		print x

def mayorque3(x):
	if x > 3:
		print "es mayor"
	else:
		print "es menor"

def mifuncion(nombre):
	print "Hola " + nombre
	
mifuncion("David Sevilla")

variable = MiClase();
variable.metodo1()
variable.metodobase()

mayorque3(56)
mayorque3(2)

elementos = ["Jorge", "Juan", "Pedro", "Pablo"]
imprimirelementos(elementos)

for x in range (10):
	print x