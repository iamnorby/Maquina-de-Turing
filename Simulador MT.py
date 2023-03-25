#Integrantes:
#Yuly Katherine Sierra -  20201678017
#Norvey Valencia Enciso - 20192678034

#Inicio Automatas Finitos Deterministas
def AFD():
    d = {}
    F = set()
    #Analiza el archivo ProgramaAFD.txt para realizar los estados
    programa = open("programaAFD.txt")
    for linea in programa:
        q, s, n = linea.split()
        if "*" in q:
            q = q.strip("*")
            F.add(q)
        d[q, s] = n
    programa.close()

    #aqui esta en programa se Automata Finito Determinista, coje lo que hay Etrada.txt y analiza segunlo anterior
    def SIMAFD(cinta, d, f, q0):
        q = q0
        for simbolo in cinta:
            q = d[q, simbolo]
        return q in F

    traducir = {False: "Rechazada", True: "Aceptada"}

    cintas = open("Entrada.txt")
    for linea in cintas:
        linea = linea.rstrip()
        print("La cinta", linea, " es ", traducir[SIMAFD(linea, d, F, "0")])
    cintas.close()

#Inicio de la maquina de turing
def turing_M(estado=None,
             vacio=None,
             reglas=[],
             cinta=[],
             final=None,
             pos=0):

    st = estado
    if not cinta: cinta = [vacio]
    if pos < 0: pos += len(cinta)
    if pos >= len(cinta) or pos < 0: raise Error("Se inicializa mal la posicion")

    reglas = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in reglas)
    """
Estado	Símbolo leído	Símbolo escrito	       Mov. 	Estado sig.
  p(s0)	       1(v0)	         x(v1)         R(dr)	     p(s1)
"""
    while True:
        print(st, '\t', end=" ")
        for i, v in enumerate(cinta):
            if i == pos:
                print("[%s]" % (v,), end=" ")
            else:
                print(v, end=" ")
        print()

        if st == final: break
        if (st, cinta[pos]) not in reglas: break

        (v1, dr, s1) = reglas[(st, cinta[pos])]
        cinta[pos] = v1  # rescribe el simbolo de la cinta

        # movimiento del cabezal
        if dr == 'L':
            if pos > 0:
                pos -= 1
            else:
                cinta.insert(0, vacio)
        if dr == 'R':
            pos += 1
            if pos >= len(cinta): cinta.append(vacio)
        st = s1

def leerprograma():
    lista1= set()
    tupla=()
    programa = open("programaMT.txt")

    for linea in programa:
        q, s, n, d, q1 = linea.split()
        tupla= q, s, n, d, q1
        lista1.add(tupla)
    programa.close()
    return lista1

def leerentrada():
    entrada = open("Entrada.txt").read()
    input = str(entrada)
    return input

def Error(Mensaje):
    print(Mensaje)
    exit(0)

with open('Entrada.txt') as myfile:
    total_lines = sum(1 for line in myfile)
    if total_lines == 1:
        print("Maquina de turing")
        turing_M(estado='0',  # estado inicial de la maquina de turing
                 vacio='_',  # simbolo blanco de el alfabeto dela cinta
                 cinta=list(leerentrada()),  # inserta los elementos en la cinta
                 final='2',  # estado valido y/o final
                 reglas=leerprograma()
                 )
    else:
        print("Maquina Automata Finito")
        AFD()