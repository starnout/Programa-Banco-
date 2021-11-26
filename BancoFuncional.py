from __future__ import print_function
import psutil

import time
start_time = time.time()

#Funcion para depositar en caso de tener tarjeta de Debito
def deposito_D(lista):
    #La variable nuevo_monto_D contiene a la funcion lambda que indica la suma de las variables "x","y" 
    nuevo_monto_D=lambda x,y:x+y
    #La funcion devuelve la suma de los valores de la posicion 1 y 2 de una lista
    return nuevo_monto_D(lista[1],lista[2])

#Funcion para depositar en caso de tener tarjeta de Credito (Sigue los mismos pasos que la funcion deposito_D)
def deposito_C(lista):
    nuevo_monto_C=lambda w,z:w+z
    return nuevo_monto_C(lista[1],lista[2])

#Funcion para retirar en caso de tener tarjeta de Debito
def retiro_D(lista):
    #La variable monto_restante_D contiene la funcion lambda que indica la resta de las variable "a","b"
    monto_restante_D=lambda a,b:a-b
    ###La funcion devuelve la resta entre el resultado de la funcion deposito_D con el valor de la posicion 2 de una lista
    return monto_restante_D(deposito_D(lista),lista[3])

#Funcion para retirar en caso de tener tarjeta de Credito
def retiro_C(lista):
    #La variable monto_restante_C contiene la funcion lambda que indica la resta de la variable "d" con el 105%(equivale a 1.05) de la variable "e" 
    monto_restante_C=lambda d,e:d-(e*1.05)
    #La funcion devuelve la resta entre el resultado de la funcion deposito_C con el valor de la posicion 3 de una lista
    return monto_restante_C(deposito_C(lista),lista[3])

#Funcion para consultar los datos de la tarjeta de Debito y sus movimientos bancarios
def consulta_D(lista):
    print("Titular de la tarjeta: ",lista[4])
    print("Tipo de tarjeta: ",lista[0])
    print("Numero de Cuenta: ",lista[5])
    print("Primera Transaccion: \n",lista[1]," soles fueron depositados. Tu saldo en ahorros es de ",deposito_D(lista)," soles")
    print("Segunda Transaccion: \n",lista[3]," soles fueron retirados. Tu saldo en ahorros es de ",retiro_D(lista)," soles")

#Funcion para consultar los datos de la tarjeta de Credito y sus movimientos bancarios
def consulta_C(lista):
    print("Titular de la tarjeta: ",lista[4])
    print("Tipo de tarjeta: ",lista[0])
    print("Numero de Cuenta: ",lista[5])
    print("Primera Transaccion:\n",lista[1]," soles fueron depositados. Tu saldo en ahorros es de ",deposito_C(lista)," soles")
    print("Segunda Transaccion:\n",lista[3]," soles fueron retirados. Tu saldo en ahorros es de ",retiro_C(lista)," soles")

def main():
    #Formato 1 = [tipo tarjeta, deposito, ahorros, retiro,titular,num. cuenta]
    cuenta_D=["debito",800,0,250,"Pedro Castillo","11223344"]
    #Formato 2 = [tipo tarjeta, deposito, saldo base, retiro,titular,num. cuenta]
    cuenta_C=["credito",800,1000,370,"Pedro Castillo","11223344"]
    print("------------------------Tarjeta 1------------------------")
    consulta_D(cuenta_D)
    print("------------------------Tarjeta 2------------------------")
    consulta_C(cuenta_C)

main()
#medir memoria en cpu y memoria virtual
print("---------------------------------RECURSOS USADOS------------------------------")
print("Porcentaje de cpu utilizada: ",psutil.cpu_percent())    
print("Memoria fisica usada: ", psutil.virtual_memory())  # physical memory usage
print('Memoria % usada:', psutil.virtual_memory()[2])
#medir el tiempo de ejecucion de todo el programa
print("Tiempo de ejecucion de todo el programa", "--- %s segundos ---" % (time.time() - start_time))
