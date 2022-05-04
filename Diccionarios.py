

let = "abecedario"

# importa el módulo
import gc
# retorna el número de objetos colectados y liberados
collected = gc.collect()
print(collected)