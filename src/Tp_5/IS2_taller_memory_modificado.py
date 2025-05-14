import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content

class FileWriterCaretaker:
    def __init__(self):
        self.history = []  # Lista para guardar hasta 4 estados

    def save(self, writer):
        # Guardar el estado actual y mantener máximo 4 estados
        if len(self.history) == 4:
            self.history.pop(0)  # Eliminar el más antiguo si hay 4
        self.history.append(writer.save())

    def undo(self, writer, index=0):
        # index=0: estado inmediato anterior
        # index=1: estado anterior a ese, etc.
        if 0 <= index < len(self.history):
            # Recuperar el estado solicitado desde el final
            memento = self.history[-(index + 1)]
            writer.undo(memento)
        else:
            print("No hay estado guardado para ese índice de undo.")

if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional III")
    writer.write("Material adicional de la clase de patrones III\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional IV")
    writer.write("Material adicional de la clase de patrones IV\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se invoca al <undo> para el estado inmediato anterior (0)")
    caretaker.undo(writer, 0)
    print("Estado actual:")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para el estado anterior a ese (1)")
    caretaker.undo(writer, 1)
    print("Estado actual:")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para el estado 3 pasos atrás (3)")
    caretaker.undo(writer, 3)
    print("Estado actual:")
    print(writer.content + "\n\n")

