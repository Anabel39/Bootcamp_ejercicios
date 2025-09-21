"""Ejercicio 1. Función contar caracteres :Crea una función que cuente el número de caracteres en una cadena de texto dada."""
cadena_texto = "Hola me llamo Annie"
longitud = len(cadena_texto)
print(longitud)

"""Ejercicio 2.  calcular_promedio: Crea una función que calcule el promedio de una lista de números."""

def calcular_promedio(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

lista_num = [1, 5, 8 , 15, 20, 43, 24, 12, 55, 99, 80]

promedio = calcular_promedio(lista_num)
print("El promedio es:", promedio)

"""Ejercicio 3. Función encontrar_duplicado: Crea una función que busque y devuelva el primer elemento duplicado en una
lista dada."""
def encontrar_duplicado(lista):
    vistos = set() 
    for elemento in lista:
        if elemento in vistos:
            return elemento  
        vistos.add(elemento)
    return None 

lista_numeros= [2,5,6,8,9,2,6,8,7]

resultado = encontrar_duplicado(lista_numeros)
if resultado is not None:
    print ('El primer duplicado es:', resultado)
else:
    print ('No hay duplicados en la lista.')

"""Ejercicio 4. Función enmascarado_datos:Crea una función que convierta una variable en una cadena de texto y
enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro."""
def enmascarado_datos(valor):
   valor_str = str(valor)
   if len(valor_str) <= 4:
       return valor_str 
   return "#" * (len(valor_str) - 4) + valor_str[-4:]

print(enmascarado_datos('apellido'))
print(enmascarado_datos('Valencia'))
print(enmascarado_datos(4567807654043212))
"""Ejercicio 5. Función es_anagrama: Crea una función que determine si dos palabras son anagramas, es decir, si
están formadas por las mismas letras pero en diferente orden."""
def es_anagrama(palabra1, palabra2):
     p1 = palabra1.replace(" ", "").lower()
     p2 = palabra2.replace(" ", "").lower()
     return sorted(p1) == sorted(p2)

print(es_anagrama('roma','amor'))
print(es_anagrama('hola', 'adios'))

"""Ejercicio 6. Función buscar_nombre :Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para 
buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
Caso de uso:
Incorpora los siguientes nombres a la lista y comprueba que la función funciona correctamente: " Jaime", "Silvia" y "Ana"""

def buscar_nombre(nombres, nombre_buscar):
    try:
        nombres = [n.strip() for n in nombres]
        nombre_buscar = nombre_buscar.strip()

        if nombre_buscar in nombres:
            print(f"El nombre '{nombre_buscar}' está en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_buscar}' no está en la lista.")
    
    except ValueError as e:
        print("Error:", e)

lista_nombres = ['Jaime', 'Silvia', 'Ana', 'Dani']

buscar_nombre(lista_nombres, 'Ana')
buscar_nombre(lista_nombres, 'Antonio')

"""Ejercicio 7.Función fibonacci :Crea una función que calcule el término n de la serie de Fibonacci utilizando recursión."""
def fibonacci(n):
    if n <= 0:
        raise ValueError("n debe ser un entero positivo")
    elif n == 1:
        return 0  # primer término
    elif n == 2:
        return 1  # segundo término
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
for i in range (1,11):
    print(f'F{i} = {fibonacci(i)}')


"""Ejercicio 8.Función encontrar_puesto_empleado :Crea una función que tome un nombre completo y una lista de empleados,
busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando 
que la persona no trabaja aquí.
Caso de uso:
empleados = [{'nombre': " Juan", 'apellido': "García", 'puesto': "Secretario"},
{'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
{'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}]"""

def encontrar_puesto_empleado(nombre_completo, empleados):
    nombre_completo = nombre_completo.strip().lower()
    for empleado in empleados:
        nombre_emp = f"{empleado['nombre'].strip()} {empleado['apellido'].strip()}".lower()
        if nombre_emp == nombre_completo:
            return f"{empleado['nombre'].strip()} {empleado['apellido'].strip()} trabaja como {empleado['puesto']}"
    return f"{nombre_completo.title()} no trabaja aquí."

empleados = empleados = [{'nombre': " Juan", 'apellido': "García", 'puesto': "Secretario"},
                        {'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
                        {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}]

print(encontrar_puesto_empleado("Mabel García", empleados))
print(encontrar_puesto_empleado("Anabel Pérez", empleados))

"""Ejercicio 9.Función cubo_numero usando lambdas: Crea una función que calcule el cubo de un número dado mediante una función lambda"""
cubo_numero_lambda = lambda x: x ** 3
print(cubo_numero_lambda(2))

"""Ejercicio 10.Función resto_division usando lambdas: Crea una función lambda que calcule el resto de la división entre dos números dados."""
resto_division_lambda = lambda a, b: a % b
print(resto_division_lambda(10, 3))

"""Ejercicio 11. Función numeros_pares usando lambdas y filter : Crea una función lambda que filtre los números pares de una lista dada.
Caso de uso: lista_numeros = [24, 56, 2.3, 19,-1, 0]"""
numeros_pares_lambda = lambda lista: list(filter(lambda x: isinstance(x, int) and x % 2 == 0, lista))

lista_numeros = [24, 56, 2.3, 19,-1, 0]

resultado = numeros_pares_lambda(lista_numeros)
print(resultado)
"""Ejercicio 12. Función numeros_suma usando lambdas y map :Crea una función lambda que sume 3 a cada número de una lista dada.
Caso de uso: lista_numeros = [24, 56, 2.3, 19,-1, 0]"""
numeros_suma3_lambda = lambda lista: list(map(lambda x: x + 3, lista))

lista_numeros = [24, 56, 2.3, 19,-1, 0]

resultado = numeros_suma3_lambda(lista_numeros)
print(resultado)

"""Ejercicio 13. Función sumar_listas usando lambdas: Crea una función lambda que sume elementos correspondientes de dos listas dadas.
Caso de uso: lista_numeros_1 = [1, 4, 5, 6 , 7 , 7] ; lista_numeros_2 = [3, 11, 34, 56] """
sumar_listas_lambda = lambda l1, l2 : list(map(lambda x, y: x+y, l1, l2))

lista_numeros_1 = [1, 4, 5, 6 , 7 , 7] ; lista_numeros_2 = [3, 11, 34, 56]

resultado = sumar_listas_lambda(lista_numeros_1, lista_numeros_2)
print(resultado)

"""Ejercicio 14. No te vayas por las ramas :Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos 
disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la
estructura del árbol.
Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
Caso de uso:
1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol."""
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []
    def crecer_tronco(self):
       self.tronco += 1
    def nueva_rama(self):
        self.ramas.append(1)
    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición incorrecta. No se puede quitar la rama.")
    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
    
mi_arbol = Arbol()
mi_arbol.crecer_tronco()
mi_arbol.nueva_rama()
mi_arbol.crecer_ramas()
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()
mi_arbol.quitar_rama(2)
print(mi_arbol.info_arbol())

"""Ejercicio 15.Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
2. Implementar el método retirar_dinero para retirar dinero del saldo delusuario. Lanzará un error en caso de no poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no 
poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo
inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Alicia".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia"."""
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente = True):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")
        self.saldo -= cantidad
        print(f"{self.nombre} retiró {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        if not otro_usuario.cuenta_corriente:
            raise ValueError(f"{otro_usuario.nombre} no tiene cuenta corriente para transferir.")
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"{otro_usuario.nombre} transfirió {cantidad} a {self.nombre}. "
              f"Saldo {self.nombre}: {self.saldo}, Saldo {otro_usuario.nombre}: {otro_usuario.saldo}")

    def agregar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente.")
        self.saldo += cantidad
        print(f"{self.nombre} agregó {cantidad}. Saldo actual: {self.saldo}")


alicia = UsuarioBanco("Alicia", 100, True)
Bob = UsuarioBanco("Bob", 50, True)

alicia.agregar_dinero(20)
alicia.transferir_dinero(Bob,80)
alicia.retirar_dinero(50)

"""Ejercicio 16. Función procesar_texto_: Descripción: Crea una función llamada procesar_texto que procesa un texto según la opción especificada:
contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la 
función procesar_texto.
Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el 
remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto.Tiene que devolver el texto con la palabra eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable
según la opción indicada.
Caso de uso:
texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
Dado el texto de ejemplo, llama a la función procesar_texto para probar sus funcionalidades:
Cuenta el número de veces que aparece cada palabra.
Reemplaza la palabra texto por relato.
Elimina la palabra ejemplo."""
def contar_palabras(texto):
    palabras = texto.lower().split()
    contador = {}
    for palabra in palabras:
        palabra = palabra.strip(".,;:!?") 
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras = [p for p in palabras if p.strip(".,;:!?") != palabra]
    return " ".join(palabras)


def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para 'reemplazar' se necesitan 2 argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError(" Para 'eliminar' se necesita 1 argumento: palabra.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa: 'contar', 'reemplazar' o 'eliminar'.")

texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."

print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "texto", "relato"))
print(procesar_texto(texto, "eliminar", "ejemplo"))
