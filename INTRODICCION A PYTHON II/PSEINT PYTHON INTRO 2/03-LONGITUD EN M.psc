Algoritmo LONGITUDENM
	Escribir "Este programa ayuda a convertir una longitud en metros a pies, yardas y millas"
	Definir Long,pies,yardas,millas Como Real
	Escribir "Ingresa la longitud en metros"
	leer Long
	Pies <- Long*3.28/1
	yardas <- Long*1.0936/1
	millas <- Long*1/1.60934
	Escribir "La longitud de metros a pies es: ", Pies
	Escribir "La longitud de metros a yardas es: ", yardas
	Escribir  "La longitud de metros a millas es: ", millas
FinAlgoritmo
