

"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>."""

""" datos={}


datos["nombre"]=input("Digite su nombre: ")
datos["edad"]=int(input("Digite su edad: "))
datos["direccion"]=input("Digite su direccion: ")
datos["telefono"]=input("Digite su telefono: ")

print(datos)

print("Mensaje: " , datos["nombre"], "tiene ", datos["edad"] ," años, vive en ", datos["direccion"], " y su número de teléfono es", datos["telefono"] )

lista=list(datos.values())

print(lista) """




""" 
diccionario={
    "Llave":"valor 1",
    "Llave 2":"valor 2",
    "Llave 3":["elem 1","elem 2","elem 3"],
    "Llave 4":{"Llave 1 D2":"Valor 1 D2","Llave 2 D2":"Valor 2 D2","Lista 2":["Elm 1 l2, Elem 2 l2"]}
    }

print(diccionario)

diccionario["Llave 2"]="1101"

print(diccionario)

diccionario["almacen"]="Tilaran"

print(diccionario)
 """

a=1
b=1
opciones={
    1:print(a+b),
    2:print(a-b),
    3:print(a*b),
    4:print(a/b)
}
print("digite una opcion ")
opt=int(input())
print("digite dos valore: ")
a=int(input())
b=int(input())

opciones[opt]