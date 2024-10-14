from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QHeaderView
from conexion import Comunicacion


class GestionarProveedores(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ventanaGestionarProveedores = uic.loadUi('ventanaGestionarProveedores/ventanaGestionarProveedores.ui', self)
        self.ventanaGestionarProveedores.botonBaseDatos.clicked.connect(self.abrirPaginaBaseDatos)
        self.ventanaGestionarProveedores.botonAgregar.clicked.connect(self.abrirPaginaAgregar)
        self.ventanaGestionarProveedores.botonActualizar.clicked.connect(self.abrirPaginaActualizar)
        self.ventanaGestionarProveedores.botonEliminar.clicked.connect(self.abrirPaginaEliminar)
        self.ventanaGestionarProveedores.botonVolver.clicked.connect(self.abrirPaginaInicio)

        self.ventanaGestionarProveedores.botonRefrescar.clicked.connect(self.refrescarBaseDatos)
        self.ventanaGestionarProveedores.botonAgregarProveedor.clicked.connect(self.agregarProveedor)
        self.ventanaGestionarProveedores.botonBuscarActualizar.clicked.connect(self.buscarActualizarProveedor)
        self.ventanaGestionarProveedores.botonActualizarProveedor.clicked.connect(self.actualizarProveedor)
        self.ventanaGestionarProveedores.botonBuscarEliminar.clicked.connect(self.buscarEliminarProveedor)
        self.ventanaGestionarProveedores.botonEliminarProveedor.clicked.connect(self.eliminarProveedor)

        self.ventanaGestionarProveedores.tablaActualizarProveedor.itemClicked.connect(self.seleccionarProveedor)
        self.ventanaGestionarProveedores.tablaEliminar.itemClicked.connect(self.seleccionarProveedorEliminar)


        self.lineEdits = {
            'id': self.ventanaGestionarProveedores.lineEditIdActualizarProveedor,
            'nombre': self.ventanaGestionarProveedores.lineEditNombreActualizarProveedor,
            'email': self.ventanaGestionarProveedores.lineEditEmailActualizarProveedor,
            'telefono': self.ventanaGestionarProveedores.lineEditTelefonoActualizarProveedor,
            'direccion': self.ventanaGestionarProveedores.lineEditDireccionActualizarProveedor
        }


        self.baseDatos = Comunicacion()
        self.tablaProveedores = self.ventanaGestionarProveedores.tablaProveedores
        self.tablaEliminar = self.ventanaGestionarProveedores.tablaEliminar


        self.refrescarBaseDatos()


    def abrirPaginaBaseDatos(self):
        self.ventanaGestionarProveedores.stackedWidget.setCurrentIndex(0)

    def abrirPaginaAgregar(self):
        self.ventanaGestionarProveedores.stackedWidget.setCurrentIndex(1)

    def abrirPaginaActualizar(self):
        self.ventanaGestionarProveedores.stackedWidget.setCurrentIndex(2)

    def abrirPaginaEliminar(self):
        self.ventanaGestionarProveedores.stackedWidget.setCurrentIndex(3)

    def abrirPaginaInicio(self):
        from menuOpciones import MenuOpciones

        self.hide()  # Oculta la ventana actual de MenuOpciones
        self.menu_window = MenuOpciones()
        self.menu_window.showMenuOpciones()  # Muestra la ventana de login


    # AQUI SE AGREGA LAS FUNCIONES PARA HACERLOS CON LA BASE DE DATOS

    def refrescarBaseDatos(self):

        datos = self.baseDatos.mostrarProveedores()
        self.tablaProveedores.setRowCount(len(datos))

        for row, proveedor in enumerate(datos):
            for col, valor in enumerate(proveedor[0:]):
                self.tablaProveedores.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))


    def agregarProveedor(self):

        id_proveedor = self.ventanaGestionarProveedores.lineEditAgregarId.text()
        nombre = self.ventanaGestionarProveedores.lineEditAgregarNombre.text()
        email = self.ventanaGestionarProveedores.lineEditAgregarEmail.text()
        telefono = self.ventanaGestionarProveedores.lineEditAgregarTelefono.text()
        direccion = self.ventanaGestionarProveedores.lineEditAgregarDireccion.text()

        print(id_proveedor, nombre, email, telefono, direccion)

        agregarProveedorBD = self.baseDatos.agregarProveedor(id_proveedor, nombre, email, telefono, direccion)

        self.ventanaGestionarProveedores.lineEditAgregarId.setText("")
        self.ventanaGestionarProveedores.lineEditAgregarNombre.setText("")
        self.ventanaGestionarProveedores.lineEditAgregarEmail.setText("")
        self.ventanaGestionarProveedores.lineEditAgregarTelefono.setText("")
        self.ventanaGestionarProveedores.lineEditAgregarDireccion.setText("")


        if agregarProveedorBD:
            print("agregado")
            self.ventanaGestionarProveedores.signalAgregar.setText("Proveedor agregado")

        else:
            print("no agregado")
            self.ventanaGestionarProveedores.signalAgregar.setText("Proveedor NO agregado")



    def buscarActualizarProveedor(self):

        proveedorBuscar = self.ventanaGestionarProveedores.lineEditBuscarActualizar.text()
        buscarProveedorBD = self.baseDatos.buscarProveedorActualizar(proveedorBuscar)
        self.ventanaGestionarProveedores.lineEditBuscarActualizar.clear()

        if len(buscarProveedorBD) == 0:
            self.ventanaGestionarProveedores.signalActualizarProveedor.setText("Proveedor NO encontrado")

        else:
            self.ventanaGestionarProveedores.signalActualizarProveedor.setText("Coincidencias encontradas")

            # MOSTRAR RESULTADOS ENCONTRADOS CUANDO SE DA A BOTON BUSCAR
            self.tablaActualizarProveedor = self.ventanaGestionarProveedores.tablaActualizarProveedor
            self.tablaActualizarProveedor.setRowCount(len(buscarProveedorBD))

            for row, proveedor in enumerate(buscarProveedorBD):
                for col, valor in enumerate(proveedor[0:]):
                    self.tablaActualizarProveedor.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))


    def seleccionarProveedor(self, item):
        row = item.row()
        columnas = ['id', 'nombre', 'email', 'telefono', 'direccion']
        for col, campo in enumerate(columnas):
            valor = self.ventanaGestionarProveedores.tablaActualizarProveedor.item(row, col).text()
            self.lineEdits[campo].setText(valor)
            print(campo, self.lineEdits[campo], valor)



    def actualizarProveedor(self):

        filaSeleccionada = self.ventanaGestionarProveedores.tablaActualizarProveedor.currentRow()

        if filaSeleccionada < 0:
            self.ventanaGestionarProveedores.signalActualizarProducto.setText("Por favor seleccione un proveedor")
            return

        idOriginal = self.ventanaGestionarProveedores.tablaActualizarProveedor.item(filaSeleccionada, 0).text()

        # Obtener los nuevos valores de los LineEdit
        nuevo_id = self.lineEdits['id'].text()
        nuevo_nombre = self.lineEdits['nombre'].text()
        nuevo_email = self.lineEdits['email'].text()
        nuevo_telefono = self.lineEdits['telefono'].text()
        nueva_direccion = self.lineEdits['direccion'].text()

        # Verificar que todos los campos tengan valor
        if not all([nuevo_id, nuevo_nombre, nuevo_email, nuevo_telefono, nueva_direccion]):
            self.ventanaGestionarProveedores.signalActualizarProducto.setText("Por favor complete todos los campos")
            return

        # Determinar si es una actualización de ID o solo de otros campos
        if idOriginal != nuevo_id:
            # Si el ID cambió, crear nuevo registro y eliminar el antiguo
            actualizacion_exitosa = self.baseDatos.actualizarProveedorConNuevoId(idOriginal,nuevo_id,nuevo_nombre,nuevo_email,nuevo_telefono,nueva_direccion)
        else:
            # Si el ID no cambió, solo actualizar los otros campos
            actualizacion_exitosa = self.baseDatos.actualizarProveedorMismoId(idOriginal,nuevo_nombre,nuevo_email,nuevo_telefono,nueva_direccion)

        if actualizacion_exitosa:
            self.ventanaGestionarProveedores.signalActualizarProveedor.setText("Proveedor actualizado")

            # Limpiar los campos después de actualizar
            for lineEdit in self.lineEdits.values():
                lineEdit.clear()


            self.ventanaGestionarProveedores.lineEditBuscarActualizar.clear()

            # Limpiar la tabla
            self.ventanaGestionarProveedores.tablaActualizarProveedor.setRowCount(0)

        else:
            self.ventanaGestionarProveedores.signalActualizarProveedor.setText("Error al actualizar")


    def buscarEliminarProveedor(self):

        proveedorBuscar = self.ventanaGestionarProveedores.lineEditBuscarEliminar.text()
        buscarProveedorenBD = self.baseDatos.buscarProveedorActualizar(proveedorBuscar)

        if len(buscarProveedorenBD) == 0:
            self.ventanaGestionarProveedores.signalEliminar.setText("Proveedor NO encontrado")

        else:
            self.ventanaGestionarProveedores.signalEliminar.setText("Coincidencias encontradas")

            # MOSTRAR RESULTADOS ENCONTRADOS CUANDO SE DA A BOTON BUSCAR
            self.tablaEliminar.setRowCount(len(buscarProveedorenBD))

            for row, proveedor in enumerate(buscarProveedorenBD):
                for col, valor in enumerate(proveedor[0:]):
                    self.tablaEliminar.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))



    def seleccionarProveedorEliminar(self, item):
        fila_seleccionada = item.row()
        print(fila_seleccionada)
        id_item = self.ventanaGestionarProveedores.tablaEliminar.item(fila_seleccionada, 0)

        if id_item is not None:
            # Obtiene el texto del ítem, que es el ID del producto
            id_proveedor = id_item.text()
            print(f"ID del proveedor seleccionado: {id_proveedor}")  # Para depuración

            # Guarda el ID del producto como un atributo de la clase
            self.id_proveedor_seleccionado = id_proveedor

            # Actualiza la señal en la interfaz
            self.ventanaGestionarProveedores.signalEliminar.setText(f"Proveedor seleccionado: {id_proveedor}")

            # Habilita el botón de eliminar
            self.ventanaGestionarProveedores.botonEliminarProveedor.setEnabled(True)
        else:
            print("No se pudo obtener el ID del proveedor")
            self.ventanaGestionarProveedores.signalEliminar.setText("Error al seleccionar el proveedor")
            self.ventanaGestionarProveedores.botonEliminarProveedor.setEnabled(False)



    def eliminarProveedor(self):
        if not hasattr(self, 'id_proveedor_seleccionado'):
            self.ventanaGestionarProveedores.signalEliminar.setText("Por favor, seleccione un proveedor primero")
            return

        try:
            # Intenta eliminar el producto de la base de datos
            if self.baseDatos.eliminarProveedor(self.id_proveedor_seleccionado):
                # Si la eliminación fue exitosa
                self.ventanaGestionarProveedores.signalEliminar.setText(
                    f"Proveedor {self.id_proveedor_seleccionado} eliminado con éxito")

                # Limpiar la tabla
                self.ventanaGestionarProveedores.tablaEliminar.setRowCount(0)

                # Limpia la selección y deshabilita el botón de eliminar
                delattr(self, 'id_proveedor_seleccionado')
                self.ventanaGestionarProveedores.botonEliminarProveedor.setEnabled(False)

                # Limpiar el campo de búsqueda
                self.ventanaGestionarProveedores.lineEditBuscarEliminar.clear()

            else:
                # Si hubo un problema al eliminar
                self.ventanaGestionarProveedores.signalEliminar.setText("Error al eliminar el proveedor")

        except Exception as e:
            # Si ocurre cualquier otro error
            print(f"Error inesperado: {e}")
            self.ventanaGestionarProveedores.signalEliminar.setText("Error inesperado al eliminar el proveedor")

        print("Operación de eliminación completada")  # Para depuración

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    menu = GestionarProveedores()
    menu.show()
    app.exec_()