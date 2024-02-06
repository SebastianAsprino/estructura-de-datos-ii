def nodo(data):
    return {'data': data, 'hijo': []}

A = nodo("A")
B = nodo("B")
C = nodo("C")
D = nodo("D")
E = nodo("E")
F = nodo("F")
G = nodo("G")
H = nodo("H")
I = nodo("I")
J = nodo("J")
K = nodo("K")
L = nodo("L")
M = nodo("M")
N = nodo("N")
O = nodo("O")
P = nodo("P")
Q = nodo("Q")
R = nodo("R")
S = nodo("S")

A['hijo'] = [B, C, D, E, F]
B['hijo'] = [G, H, I]
F['hijo'] = [J, K, L]
H['hijo'] = [M, N, O, P]
K['hijo'] = [Q, R]
N['hijo'] = [S]


# print("Los hijos de A son:")
# for child in A['hijo']:
#     print(child['data'])

def imprimir_arbol(nodo, nivel=0):
    if nodo is None:
        return

    print("|   " * nivel + "|-- " + nodo['data'])

    for hijo in nodo['hijo']:
        imprimir_arbol(hijo, nivel + 1)

imprimir_arbol(A)

def arbol_nario_a_binario(nodo):
    if nodo is None:
        return None
    
    nodo_binario = {
        'data': nodo['data'],
        'Hijo_Izquierda': None,
        'Hijo_Derecha': None
    }
    
    if len(nodo['hijo']) > 0:
        hijo = nodo['hijo'][0]
        nodo_binario['Hijo_Izquierda'] = arbol_nario_a_binario(hijo)
        
        for i in range(1, len(nodo['hijo'])):
            hijo = nodo['hijo'][i]
            hijo_binario = arbol_nario_a_binario(hijo)
            nodo_actual = nodo_binario
            while nodo_actual['Hijo_Derecha'] is not None:
                nodo_actual = nodo_actual['Hijo_Derecha']
            nodo_actual['Hijo_Derecha'] = hijo_binario
    
    return nodo_binario

arbol_binario = arbol_nario_a_binario(A)

def imprimir_arbol_binario(nodo, nivel=0):
    if nodo is None:
        return

    print("|   " * nivel + "|-- " + nodo['data'])

    imprimir_arbol_binario(nodo['Hijo_Izquierda'], nivel + 1)
    imprimir_arbol_binario(nodo['Hijo_Derecha'], nivel + 1)

imprimir_arbol_binario(arbol_binario)

