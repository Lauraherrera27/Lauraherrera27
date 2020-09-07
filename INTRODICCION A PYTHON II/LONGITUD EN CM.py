print ("Este programa ayuda a convertir una longitud en cm a milímetros, decímetro, decámetro, hectómetro y kilometros")

Long= float(input("ingresa la longitud en cm: "))

Mm= (Long*10/1)
Dm= (Long*1/10)
Dam= (Long*1/1000)
Hm= (Long*1/100)
Km= (Long*1/100000)
print ("la longitud de cm a mm es: ", Mm) 
print ("la longitud de cm a dm es:", Dm)
print ("la longitud de cm a dam es: ",Dam)
print ("la longitud de cm a hm es: ", Hm)
print ("la longitud de cm a km es: ", Km)

