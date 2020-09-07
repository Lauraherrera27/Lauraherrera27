print ("Este programa permite que el usuario le de el valor de una compra de una misma referencia al cliente con el iva incluido")

VU= float(input("ingresa el valor unitario del producto: "))
CDP= float(input("ingresa la cantidad de productos: "))

Total= (VU*CDP)
IVA= ((Total*16)/100)
CLI= (Total+IVA)
print ("El valor total de los productos mas el IVA es: ", CLI)