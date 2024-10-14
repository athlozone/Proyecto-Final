from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QHeaderView
from conexion import Comunicacion

class GestionarClientes(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ventanaGestionarClientes = uic.loadUi('ventanaGestionarClientes/ventanaGestionarClientes.ui', self)
        self.ventanaGestionarClientes.botonBaseDatos.clicked.connect(self.abrirPaginaBaseDatos)
        self.ventanaGestionarClientes.botonAgregar.clicked.connect(self.abrirPaginaAgregar)
        self.ventanaGestionarClientes.botonActualizar.clicked.connect(self.abrirPaginaActualizar)
        self.ventanaGestionarClientes.botonEliminar.clicked.connect(self.abrirPaginaEliminar)
        self.ventanaGestionarClientes.botonVolver.clicked.connect(self.abrirPaginaInicio)

        self.ventanaGestionarClientes.botonRefrescar.clicked.connect(self.refrescarBaseDatos)
        self.ventanaGestionarClientes.botonAgregarCliente.clicked.connect(self.agregarCliente)
        self.ventanaGestionarClientes.botonBuscarActualizar.clicked.connect(self.buscarActualizarCliente)
        self.ventanaGestionarClientes.botonActualizarCliente.clicked.connect(self.actualizarCliente)
        self.ventanaGestionarClientes.botonBuscarEliminar.clicked.connect(self.buscarEliminarCliente)
        self.ventanaGestionarClientes.botonEliminarCliente.clicked.connect(self.eliminarCliente)

        self.ventanaGestionarClientes.tablaActualizar.itemClicked.connect(self.seleccionarCliente)
        self.ventanaGestionarClientes.tablaEliminar.itemClicked.connect(self.seleccionarClienteEliminar)

        self.lineEdits = {
            'id': self.ventanaGestionarClientes.lineEditIdActualizarCliente,
            'nombre': self.ventanaGestionarClientes.lineEditNombreActualizarCliente,
            'email': self.ventanaGestionarClientes.lineEditEmailActualizarCliente,
            'telefono': self.ventanaGestionarClientes.lineEditTelefonoActualizarCliente,
            'direccion': self.ventanaGestionarClientes.lineEditDireccionActualizarCliente
        }

        # LLAMAR ARCHÍVO CONEXION PARA ESTABLECER LA CONEXION CON LA BASE DE DATOS
        self.baseDatos = Comunicacion()
        self.tablaClientes = self.ventanaGestionarClientes.tablaClientes
        self.tablaEliminar = self.ventanaGestionarClientes.tablaEliminar

        self.refrescarBaseDatos()




    def abrirPaginaBaseDatos(self):
        self.ventanaGestionarClientes.stackedWidget.setCurrentIndex(0)

    def abrirPaginaAgregar(self):
        self.ventanaGestionarClientes.stackedWidget.setCurrentIndex(1)

    def abrirPaginaActualizar(self):
        self.ventanaGestionarClientes.stackedWidget.setCurrentIndex(2)

    def abrirPaginaEliminar(self):
        self.ventanaGestionarClientes.stackedWidget.setCurrentIndex(3)

    def abrirPaginaInicio(self):
        from menuOpciones import MenuOpciones

        self.hide()  # Oculta la ventana actual de MenuOpciones
        self.menu_window = MenuOpciones()
        self.menu_window.showMenuOpciones()  # Muestra la ventana de login


    # AQUI SE AGREGA LAS FUNCIONES PARA HACERLOS CON LA BASE DE DATOS

    def refrescarBaseDatos(self):

        datos = self.baseDatos.mostrarClientes()
        self.tablaClientes.setRowCount(len(datos))

        for row, cliente in enumerate(datos):
            for col, valor in enumerate(cliente[0:]):
                self.tablaClientes.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))


    def agregarCliente(self):

        id_clientes = self.ventanaGestionarClientes.lineEditAgregarId.text()
        nombre = self.ventanaGestionarClientes.lineEditAgregarNombre.text()
        email = self.ventanaGestionarClientes.lineEditAgregarEmail.text()
        telefono = self.ventanaGestionarClientes.lineEditAgregarTelefono.text()
        direccion = self.ventanaGestionarClientes.lineEditAgregarDireccion.text()

        print(id_clientes, nombre, email, telefono, direccion)

        agregarClienteBD = self.baseDatos.agregarCliente(id_clientes, nombre, email, telefono, direccion)

        self.ventanaGestionarClientes.lineEditAgregarId.setText("")
        self.ventanaGestionarClientes.lineEditAgregarNombre.setText("")
        self.ventanaGestionarClientes.lineEditAgregarEmail.setText("")
        self.ventanaGestionarClientes.lineEditAgregarTelefono.setText("")
        self.ventanaGestionarClientes.lineEditAgregarDireccion.setText("")

        if agregarClienteBD:
            print("agregado")
            self.ventanaGestionarClientes.signalAgregar.setText("Cliente agregado")

        else:
            print("no agregado")
            self.ventanaGestionarClientes.signalAgregar.setText("Cliente NO agregado")


    def buscarActualizarCliente(self):

        clienteBuscar = self.ventanaGestionarClientes.lineEditBuscarActualizar.text()
        buscarClienteBD = self.baseDatos.buscarClienteActualizar(clienteBuscar)
        self.ventanaGestionarClientes.lineEditBuscarActualizar.clear()

        if len(buscarClienteBD) == 0:
            self.ventanaGestionarClientes.signalActualizarCliente.setText("Cliente NO encontrado")

        else:
            self.ventanaGestionarClientes.signalActualizarCliente.setText("Coincidencias encontradas")

            # MOSTRAR RESULTADOS ENCONTRADOS CUANDO SE DA A BOTON BUSCAR
            self.tablaActualizarCliente = self.ventanaGestionarClientes.tablaActualizar
            self.tablaActualizarCliente.setRowCount(len(buscarClienteBD))

            for row, cliente in enumerate(buscarClienteBD):
                for col, valor in enumerate(cliente[0:]):
                    self.tablaActualizarCliente.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))


    def seleccionarCliente(self, item):
        row = item.row()
        columnas = ['id', 'nombre', 'email', 'telefono', 'direccion']
        for col, campo in enumerate(columnas):
            valor = self.ventanaGestionarClientes.tablaActualizar.item(row, col).text()
            self.lineEdits[campo].setText(valor)


    def actualizarCliente(self):

        filaSeleccionada = self.ventanaGestionarClientes.tablaActualizar.currentRow()

        if filaSeleccionada < 0:
            self.ventanaGestionarClientes.signalActualizarCliente.setText("Por favor seleccione un cliente")
            return

        idOriginal = self.ventanaGestionarClientes.tablaActualizar.item(filaSeleccionada, 0).text()

        # Obtener los nuevos valores de los LineEdit
        nuevo_id = self.lineEdits['id'].text()
        nuevo_nombre = self.lineEdits['nombre'].text()
        nuevo_email = self.lineEdits['email'].text()
        nuevo_telefono = self.lineEdits['telefono'].text()
        nueva_direccion = self.lineEdits['direccion'].text()

        # Verificar que todos los campos tengan valor
        if not all([nuevo_id, nuevo_nombre, nuevo_email, nuevo_telefono, nueva_direccion]):
            self.ventanaGestionarClientes.signalActualizarCliente.setText("Por favor complete todos los campos")
            return

        # Determinar si es una actualización de ID o solo de otros campos
        if idOriginal != nuevo_id:
            # Si el ID cambió, crear nuevo registro y eliminar el antiguo
            actualizacion_exitosa = self.baseDatos.actualizarClienteConNuevoId(idOriginal,nuevo_id,nuevo_nombre,nuevo_email,nuevo_telefono,nueva_direccion)
        else:
            # Si el ID no cambió, solo actualizar los otros campos
            actualizacion_exitosa = self.baseDatos.actualizarClienteMismoId(idOriginal,nuevo_nombre,nuevo_email,nuevo_telefono,nueva_direccion)

        if actualizacion_exitosa:
            self.ventanaGestionarClientes.signalActualizarCliente.setText("Cliente actualizado")

            # Limpiar los campos después de actualizar
            for lineEdit in self.lineEdits.values():
                lineEdit.clear()


            self.ventanaGestionarClientes.lineEditBuscarActualizar.clear()

            # Limpiar la tabla
            self.ventanaGestionarClientes.tablaActualizar.setRowCount(0)

        else:
            self.ventanaGestionarClientes.signalActualizarCliente.setText("Error al actualizar")


    def buscarEliminarCliente(self):

        clienteBuscar = self.ventanaGestionarClientes.lineEditBuscarEliminar.text()
        buscarClienteenBD = self.baseDatos.buscarClienteActualizar(clienteBuscar)

        if len(buscarClienteenBD) == 0:
            self.ventanaGestionarClientes.signalEliminar.setText("Cliente NO encontrado")

        else:
            self.ventanaGestionarClientes.signalEliminar.setText("Coincidencias encontradas")

            # MOSTRAR RESULTADOS ENCONTRADOS CUANDO SE DA A BOTON BUSCAR
            self.tablaEliminar.setRowCount(len(buscarClienteenBD))

            for row, cliente in enumerate(buscarClienteenBD):
                for col, valor in enumerate(cliente[0:]):
                    self.tablaEliminar.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))


    def seleccionarClienteEliminar(self, item):
        fila_seleccionada = item.row()
        id_item = self.ventanaGestionarClientes.tablaEliminar.item(fila_seleccionada, 0)

        if id_item is not None:
            # Obtiene el texto del ítem, que es el ID del producto
            id_clientes = id_item.text()
            print(f"ID del cliente seleccionado: {id_clientes}")  # Para depuración

            # Guarda el ID del producto como un atributo de la clase
            self.id_cliente_seleccionado = id_clientes

            # Actualiza la señal en la interfaz
            self.ventanaGestionarClientes.signalEliminar.setText(f"Cliente seleccionado: {id_clientes}")

            # Habilita el botón de eliminar
            self.ventanaGestionarClientes.botonEliminarCliente.setEnabled(True)
        else:
            print("No se pudo obtener el ID del cliente")
            self.ventanaGestionarClientes.signalEliminar.setText("Error al seleccionar el cliente")
            self.ventanaGestionarClientes.botonEliminarCliente.setEnabled(False)


    def eliminarCliente(self):
        if not hasattr(self, 'id_cliente_seleccionado'):
            self.ventanaGestionarClientes.signalEliminar.setText("Por favor, seleccione un cliente primero")
            return

        try:
            # Intenta eliminar el producto de la base de datos
            if self.baseDatos.eliminarCliente(self.id_cliente_seleccionado):
                # Si la eliminación fue exitosa
                self.ventanaGestionarClientes.signalEliminar.setText(
                    f"cliente {self.id_cliente_seleccionado} eliminado con éxito")

                # Limpiar la tabla
                self.ventanaGestionarClientes.tablaEliminar.setRowCount(0)

                # Limpia la selección y deshabilita el botón de eliminar
                delattr(self, 'id_cliente_seleccionado')
                self.ventanaGestionarClientes.botonEliminarCliente.setEnabled(False)

                # Limpiar el campo de búsqueda
                self.ventanaGestionarClientes.lineEditBuscarEliminar.clear()

            else:
                # Si hubo un problema al eliminar
                self.ventanaGestionarClientes.signalEliminar.setText("Error al eliminar el cliente")

        except Exception as e:
            # Si ocurre cualquier otro error
            print(f"Error inesperado: {e}")
            self.ventanaGestionarClientes.signalEliminar.setText("Error inesperado al eliminar el cliente")

        print("Operación de eliminación completada")  # Para depuración

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    menu = GestionarClientes()
    menu.show()
    app.exec_()