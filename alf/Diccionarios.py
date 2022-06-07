

let = "abecedario"

# importa el módulo
import gc
# retorna el número de objetos colectados y liberados
collected = gc.collect()
print(collected)
#2

monedas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")

# if moneda.title() in monedas:
#     print(monedas[moneda.title()])

# else :
#     print("La divisa no se encuentra")

#b
# if monedas.get(moneda):
#     print (monedas.get(moneda))
# else: print("no se encontro la divisa")

#c
#print(monedas.get(moneda.title(),"La divisa no se encuentra"))


#3
frutas = {
    "Plátano" :1.35,
    "Manzana":0.80,
    "Pera" :0.85,
    "Naranja" :0.70
    }

frutaelegida = input("elige una fruta")
kilos = input("elige una cantidad")

