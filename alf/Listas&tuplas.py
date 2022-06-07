# 1
# asignituras = ["Matemáticas","Física","Química",", Historia","Lengua"]
# notas = [6,2,7,3,4]
# 2
# print("yo estudio,",asignituras[1])

# 3
# notas=[]
# for i in asignituras:
#     letnotas = input(f"cual es la nota que sacaste en, {i}:  ")
#     notas.append(letnotas)

# j = 0
# while(j < len(asignituras)):
#     print("En",asignituras[j],"has sacado",notas[j])
#     j+=1

# 4
# ganadornro=[]
# for i in range(0,5):
#     ganadornro.append(int(input("cuales son los numeros ganadores:  ")))

# ganadornro.sort()
# print("Los nro ganadores de la loteria son:  ",ganadornro)

# 5
# lista = []
# for i in range(0,11):
#     lista.append(i)

# lista.sort(reverse=True)
# print(lista)

#6
# asignituras = ["Matemáticas","Física","Química","Historia","Lengua"]
# notas = [6,2,7,3,4]

# tremestre = list(zip(asignituras,notas))
# print(tremestre)

# materias_Repetir=[]
# for i, j in tremestre:
#     print(i,j)
#     if j < 6:
#         materias_Repetir.append(i)
#         #print(f"{i}: {j} millones de habitantes.")
# print(f"las materias que tienes que repetir son:",str(materias_Repetir))

#7

# minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
# posicion = []
# for i in range(1,len(minus)):
#     if i % 3 == 0:
#         posicion.append(i)

# posicion.sort(reverse=True)
# print(posicion)
# for i in posicion:
#     del minus[i]
# print(posicion)
# print(minus)


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # for i in range(len(alphabet),-1, -1):
# #     if i % 3 == 0:
# #         alphabet.pop(i-1)
# # print(alphabet)

# for i in range(len(alphabet),1,-1):
#     if i % 3 == 0:
#         del alphabet[i-1]

# print(alphabet)

#8
# def espalindromo(a):
#     a = a.replace (" ","")
#     if a == a[::-1]:
#         print("si es palidromo")
#     else:
#         print("No es palindromo")
# inputer = input("ingresa una palabra:  ")

# try:
#     if len(inputer) == 0:
#         raise ValueError("Debes ingresar un string")
    
#     if inputer.isnumeric():
#         raise TypeError("Debes ingresar Texto")
#     espalindromo(inputer)
# except ValueError as ve:
#     print(ve)
# except TypeError as tp:
#     print(tp)


#9

# let = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
# select = input("elige una letra")
# count = 0
# for i,j in enumerate(let):
#     print(i,j)
#     if j == select:
#         count +=1
# print(f"la cantidad que aparece la letra en el parrafo son:{count}")

#10

# precios = [50, 75, 46, 22, 80, 65, 8]
# precios.sort()
# print(f"el menor de los precios es: {precios[0]}\nel mayor es: {precios[-1]}")

#11
#EJERCICIO DEUDA

#12 EJERCICIO DEUDA

# MATRIZ_A = [[1,2,3],[4,5,6]]
# MATRIZ_B = [[-1,0],[0,1],[1,1]]
# suma = 0

# for i in MATRIZ_A:
#     print(i,"i en matriz_a")
#     for j in i:
#         print(j)
#         for ii in MATRIZ_B:
#             print(ii,"ii en matriz b")
#             for jj in ii:
#                 print(jj,"jj")
#                 suma = suma + (j*jj)
# print(suma)

#13 EJERCICIO DEUDA
