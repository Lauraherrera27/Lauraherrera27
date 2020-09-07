Algoritmo LONGITUDENCM
	Escribir "Este programa ayuda a convertir una longitud en cm a milímetros, decímetro, decámetro, hectómetro y kilometros"
	Definir Long,Mm,Dm,Dam,Hm,Km Como Real
	Escribir "Ingresa la longitud en cm"
	Leer Long
	Mm= (Long*10/1)
	Dm= (Long*1/10)
	Dam= (Long*1/1000)
	Hm= (Long*1/100)
	Km= (Long*1/100000)
	Escribir "La longitud de cm a mm es: ", Mm
	Escribir "La longitud de cm a dm es:", Dm
	Escribir "La longitud de cm a dam es: ",Dam
	Escribir "La longitud de cm a hm es: ", Hm
	Escribir "La longitud de cm a km es: ", Km
FinAlgoritmo
