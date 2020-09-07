print ("Este programa permite sacar el salario que se le paga a un empleado descontando el 10% de pension y el 15% de salud")

SLD= float(input("ingresa el salario diario: "))
Dias= float(input("ingresa el numeros de dias trabajados: "))

Total= (SLD*Dias)
Pension= ((Total*1)/100)
Salud= ((Total*0.15)/100)
Empl= (Total-Pension-Salud)
print ("El total a pagar al empleado es: ", Empl)