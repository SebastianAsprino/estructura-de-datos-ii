class NodoDoble:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def agregar_al_final(head, data):
    if not head:
        return NodoDoble(data)
    nodo_ac = head
    while nodo_ac.next:
        nodo_ac = nodo_ac.next
    nuevo_nodo = NodoDoble(data)
    nodo_ac.next = nuevo_nodo
    nuevo_nodo.prev = nodo_ac
    return head

def delete(head, value):
    if head and head.data == value:
        if head.next:
            head.next.prev = None
        return head.next
    nodo_ac = head
    while nodo_ac and nodo_ac.data != value:
        nodo_ac = nodo_ac.next
    if nodo_ac:
        if nodo_ac.next:
            nodo_ac.next.prev = nodo_ac.prev
        if nodo_ac.prev:
            nodo_ac.prev.next = nodo_ac.next
    return head

def search(head, value):
    nodo_ac = head
    while nodo_ac:
        if nodo_ac.data == value:
            return True
        nodo_ac = nodo_ac.next
    return False

def display(head):
    nodo_ac = head
    while nodo_ac:
        print(nodo_ac.data, end=" <-> ")
        nodo_ac = nodo_ac.next
    print("None")

# Ejemplo de uso
if __name__ == "__main__":
    linked_list = None
    linked_list = agregar_al_final(linked_list, 1)
    linked_list = agregar_al_final(linked_list, 2)
    linked_list = agregar_al_final(linked_list, 3)
    linked_list = agregar_al_final(linked_list, 4)
    linked_list = agregar_al_final(linked_list, 5)

    print("Lista inicial:")
    display(linked_list)

    linked_list = delete(linked_list, 3)
    print("Después de eliminar el nodo con valor 3:")
    display(linked_list)

    print("¿El valor 4 está en la lista?", search(linked_list, 4))
    print("¿El valor 6 está en la lista?", search(linked_list, 6))
