# Sistema de gestión de pedidos
from collections import deque

cola = deque()


def registrar_solicitud(codigo, cliente):
    cola.append((codigo, cliente))
    print(f"Solicitud {codigo} de {cliente} registrada")


def atender_solicitud():
    if not cola:
        print("No hay solicitudes para atender")
        return
    codigo, cliente = cola.popleft()
    print(f"Atendida: {codigo} - {cliente}")


def mostrar_pendientes():
    if not cola:
        print("Cola vacia")
    else:
        print("Pendientes: ", list(cola))


# -LIFO
pila = []


def registrar_despacho(cod_op, cod_prod):
    pila.append((cod_op, cod_prod))
    print(f"Despacho {cod_op} (producto {cod_prod}) registrado")


def consultar_despachos():
    if not pila:
        print("Pila vacía")
    else:
        print("Despachos (cima → base):", list(reversed(pila)))


def retirar_despacho():
    if not pila:
        print("No hay despachos para retirar")
        return
    op, prod = pila.pop()
    print(f"Retirado: {op} (producto {prod})")

# Árbol BST


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self._insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._insertar(nodo.der, valor)
        return nodo

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._buscar(nodo.izq, valor)
        return self._buscar(nodo.der, valor)

    def inorden(self):
        res = []
        self._inorden(self.raiz, res)
        return res

    def _inorden(self, nodo, res):
        if nodo:
            self._inorden(nodo.izq, res)
            res.append(nodo.valor)
            self._inorden(nodo.der, res)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izq = self._eliminar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar(nodo.der, valor)
        else:
            if nodo.izq is None:
                return nodo.der
            if nodo.der is None:
                return nodo.izq
            # sucesor inorden
            sucesor = nodo.der
            while sucesor.izq:
                sucesor = sucesor.izq
            nodo.valor = sucesor.valor
            nodo.der = self._eliminar(nodo.der, sucesor.valor)
        return nodo


arbol = BST()

# Datos iniciales
registrar_solicitud("P001", "Estudiante1")
registrar_solicitud("P002", "Estudiante2")
registrar_solicitud("P003", "Estudiante3")

registrar_despacho("D001", "PROD-A")
registrar_despacho("D002", "PROD-B")
registrar_despacho("D003", "PROD-C")

for cod in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(cod)

# - Menú


def menu():
    while True:
        print("\n- MENÚ -")
        print("1. Registrar solicitud")
        print("2. Atender solicitud")
        print("3. Mostrar pendientes")
        print("4. Registrar despacho")
        print("5. Consultar despachos")
        print("6. Retirar último despacho")
        print("7. Insertar código producto")
        print("8. Buscar código")
        print("9. Mostrar inorden")
        print("10. Eliminar código")
        print("0. Salir")
        op = input("Opción: ").strip()

        if op == "1":
            c = input("Código: ")
            n = input("Cliente: ")
            registrar_solicitud(c, n)
        elif op == "2":
            atender_solicitud()
        elif op == "3":
            mostrar_pendientes()
        elif op == "4":
            o = input("Código operación: ")
            p = input("Código producto: ")
            registrar_despacho(o, p)
        elif op == "5":
            consultar_despachos()
        elif op == "6":
            retirar_despacho()
        elif op == "7":
            try:
                v = int(input("Código numérico: "))
                arbol.insertar(v)
                print("Insertado.")
            except ValueError:
                print("Debe ser número.")
        elif op == "8":
            try:
                v = int(input("Código a buscar: "))
                print("Existe" if arbol.buscar(v) else "No existe")
            except ValueError:
                print("Debe ser número.")
        elif op == "9":
            print("Inorden:", arbol.inorden())
        elif op == "10":
            try:
                v = int(input("Código a eliminar: "))
                arbol.eliminar(v)
                print("Eliminado (si existía).")
            except ValueError:
                print("Debe ser número.")
        elif op == "0":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
