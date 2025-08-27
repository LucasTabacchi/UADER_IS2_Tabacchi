# Tabla de transiciones del AFD mínimo, ahora con columna "otro" para caracteres no válidos
transiciones = {
    "A": {"A-Z": "B", "a-z": "muerto", "0-9": "muerto", "otro": "muerto"},
    "B": {"A-Z": "CD", "a-z": "CD", "0-9": "E", "otro": "muerto"},
    "CD": {"A-Z": "muerto", "a-z": "muerto", "0-9": "FGH", "otro": "muerto"},
    "E": {"A-Z": "FGH", "a-z": "FGH", "0-9": "I", "otro": "muerto"},
    "FGH": {"A-Z": "muerto", "a-z": "muerto", "0-9": "JKLM", "otro": "muerto"},
    "I": {"A-Z": "JKLM", "a-z": "JKLM", "0-9": "muerto", "otro": "muerto"},
    "JKLM": {"A-Z": "muerto", "a-z": "NOP", "0-9": "muerto", "otro": "muerto"},
    "NOP": {"A-Z": "muerto", "a-z": "muerto", "0-9": "muerto", "otro": "muerto"},
    "muerto": {"A-Z": "muerto", "a-z": "muerto", "0-9": "muerto", "otro": "muerto"},
}

# Clasifica un carácter como "A-Z", "a-z", "0-9" o "otro"
def clasificar_caracter(car):
    if car.isupper():
        return "A-Z"
    elif car.islower():
        return "a-z"
    elif car.isdigit():
        return "0-9"
    else:
        return "otro"  # Nuevo: símbolo no permitido

# Función que reconoce si una cadena es válida según el AFD
def reconocedor(cadena):
    estado = "A"  # Estado inicial

    for caracter in cadena:
        clase = clasificar_caracter(caracter) #devuelve a-z, A-Z, 0-9 O otro para cada carácter de la cadena
        estado = transiciones[estado][clase]  # ejemplo:["A"]["A-Z"] que devuelve "B"

        # if estado == "muerto":
        #     return False

    return estado == "NOP"  # Solo acepta si termina en estado final 
                            #(esto retorna TRUE cuando la cadena es aceptada(osea termina en el estado final))



print("Reconocedor de cadenas según el AFD mínimo.")
print("Ingresá una cadena para verificar si es aceptada (o escribí 'salir' para terminar).")
print("Nota: símbolos como @, #, !, espacio, etc., hacen que la cadena se rechace.")

while True:
    cadena = input(">> Ingresá una cadena: ")

    if cadena.lower() == "salir":
        print("Programa finalizado.")
        break

    if reconocedor(cadena):
        print("Cadena ACEPTADA por el AFD.")
    else:
        print("Cadena RECHAZADA por el AFD.")