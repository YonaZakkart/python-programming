# ÁRBOL BINARIO DE BÚSQUEDA (ABB): Gestión de empleados por ID
# Regla: IDs menores a la izquierda, IDs mayores a la derecha
# Operaciones: insertar, buscar, actualizar, recorrido inorder, eliminar

class NodoEmpleado:
    def __init__(self, id_empleado, nombre, cargo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.cargo = cargo
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None   # árbol vacío al inicio

    def insertar(self, id_empleado, nombre, cargo):
        # Si el árbol está vacío, el nuevo nodo es la raíz
        if self.raiz is None:
            self.raiz = NodoEmpleado(id_empleado, nombre, cargo)
        else:
            self._insertar_recursivo(self.raiz, id_empleado, nombre, cargo)

    def _insertar_recursivo(self, nodo_actual, id_empleado, nombre, cargo):
        # ID menor: va por la izquierda
        if id_empleado < nodo_actual.id_empleado:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoEmpleado(
                    id_empleado, nombre, cargo)
            else:
                self._insertar_recursivo(
                    nodo_actual.izquierdo, id_empleado, nombre, cargo)
        # ID mayor: va por la derecha
        elif id_empleado > nodo_actual.id_empleado:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoEmpleado(id_empleado, nombre, cargo)
            else:
                self._insertar_recursivo(
                    nodo_actual.derecho, id_empleado, nombre, cargo)
        else:
            # Si el ID ya existe, actualizamos los datos en vez de duplicar
            nodo_actual.nombre = nombre
            nodo_actual.cargo = cargo

    def buscar(self, id_empleado):
        return self._buscar_recursivo(self.raiz, id_empleado)

    def _buscar_recursivo(self, nodo_actual, id_empleado):
        # Caso base: no existe (None) o lo encontramos
        if nodo_actual is None or nodo_actual.id_empleado == id_empleado:
            return nodo_actual
        # Decidimos por qué rama seguir comparando IDs
        if id_empleado < nodo_actual.id_empleado:
            return self._buscar_recursivo(nodo_actual.izquierdo, id_empleado)
        return self._buscar_recursivo(nodo_actual.derecho, id_empleado)

    def actualizar(self, id_empleado, nuevo_nombre, nuevo_cargo):
        nodo = self.buscar(id_empleado)
        if nodo:
            nodo.nombre = nuevo_nombre
            nodo.cargo = nuevo_cargo
            return True    # actualizado
        return False       # no existe ese ID

    def recorrido_inorder(self):
        self._inorder_recursivo(self.raiz)

    def _inorder_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._inorder_recursivo(nodo_actual.izquierdo)
            print(
                f"ID: {nodo_actual.id_empleado} | Nombre: {nodo_actual.nombre} | Cargo: {nodo_actual.cargo}")
            self._inorder_recursivo(nodo_actual.derecho)

    def eliminar(self, id_empleado):
        self.raiz = self._eliminar_recursivo(self.raiz, id_empleado)

    def _eliminar_recursivo(self, nodo_actual, id_empleado):
        if nodo_actual is None:
            return nodo_actual

        # Buscamos el nodo a eliminar
        if id_empleado < nodo_actual.id_empleado:
            nodo_actual.izquierdo = self._eliminar_recursivo(
                nodo_actual.izquierdo, id_empleado)
        elif id_empleado > nodo_actual.id_empleado:
            nodo_actual.derecho = self._eliminar_recursivo(
                nodo_actual.derecho, id_empleado)
        else:
            # Caso 1 y 2: sin hijos o con un solo hijo -> lo reemplaza el hijo existente
            if nodo_actual.izquierdo is None:
                return nodo_actual.derecho
            elif nodo_actual.derecho is None:
                return nodo_actual.izquierdo

            # Caso 3: dos hijos -> buscamos el sucesor (menor del subárbol derecho)
            sucesor = self._obtener_minimo(nodo_actual.derecho)
            # Copiamos los datos del sucesor al nodo actual
            nodo_actual.id_empleado = sucesor.id_empleado
            nodo_actual.nombre = sucesor.nombre
            nodo_actual.cargo = sucesor.cargo
            # Eliminamos el sucesor original del subárbol derecho
            nodo_actual.derecho = self._eliminar_recursivo(
                nodo_actual.derecho, sucesor.id_empleado)

        return nodo_actual

    def _obtener_minimo(self, nodo_actual):
        # El menor siempre está más a la izquierda
        actual = nodo_actual
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual


if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()

    # Insertar empleados
    arbol.insertar(105, "Carlos Ramos", "Backend")
    arbol.insertar(102, "Ana López", "Analista")
    arbol.insertar(110, "Beatriz Gómez", "PM")
    arbol.insertar(101, "Diego Martínez", "Soporte")

    # Mostrar ordenados por ID
    print("--- Listado Inorder ---")
    arbol.recorrido_inorder()

    # Actualizar el cargo de Diego
    arbol.actualizar(101, "Diego Martínez", "SysAdmin")

    # Eliminar a Ana (tiene un hijo: caso 2)
    arbol.eliminar(102)

    print("\n--- Después de actualizar y eliminar ---")
    arbol.recorrido_inorder()
