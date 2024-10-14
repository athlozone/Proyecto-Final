from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QHeaderView
from conexion import Comunicacion


class ControlarStock(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ventanaControlarStock = uic.loadUi('ventanaControlarStock/ventanaControlarStock.ui', self)
        self.ventanaControlarStock.botonBaseDatos.clicked.connect(self.abrirPaginaBaseDatos)
        self.ventanaControlarStock.botonAgregar.clicked.connect(self.abrirPaginaAgregar)
        self.ventanaControlarStock.botonActualizar.clicked.connect(self.abrirPaginaActualizar)
        self.ventanaControlarStock.botonEliminar.clicked.connect(self.abrirPaginaEliminar)
        self.ventanaControlarStock.botonVolver.clicked.connect(self.abrirPaginaInicio)

        self.ventanaControlarStock.botonRefrescar.clicked.connect(self.refrescarBaseDatos)
        self.ventanaControlarStock.botonAgregarProducto.clicked.connect(self.agregarProducto)
        self.ventanaControlarStock.botonBuscarActualizar.clicked.connect(self.buscarActualizarProducto)
        self.ventanaControlarStock.botonActualizarProducto.clicked.connect(self.actualizarProducto)
        self.ventanaControlarStock.botonBuscarEliminar.clicked.connect(self.buscarEliminarProducto)
        self.ventanaControlarStock.botonEliminarProducto.clicked.connect(self.eliminarProducto)

        self.ventanaControlarStock.tablaProductosActualizar.itemClicked.connect(self.seleccionarProducto)
        self.ventanaControlarStock.tablaEliminar.itemClicked.connect(self.seleccionarProductoEliminar)

        self.lineEdits = {
            'id': self.ventanaControlarStock.lineEditIdActualizarStock,
            'nombre': self.ventanaControlarStock.lineEditNombreActualizarStock,
            'descripcion': self.ventanaControlarStock.lineEditDescripcionActualizarStock,
            'precio': self.ventanaControlarStock.lineEditPrecioActualizarStock,
            'cantidad_stock': self.ventanaControlarStock.lineEditCantidadStockActualizarStock,
            'categoria': self.ventanaControlarStock.lineEditCategoriaActualizarStock
        }


        self.baseDatos = Comunicacion()
        self.tablaProductos = self.ventanaControlarStock.tablaProductos
        self.tablaEliminar = self.ventanaControlarStock.tablaEliminar
        self.tablaProductos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tablaProductos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.refrescarBaseDatos()

    def abrirPaginaBaseDatos(self):
        self.ventanaControlarStock.stackedWidget.setCurrentIndex(0)

    def abrirPaginaAgregar(self):
        self.ventanaControlarStock.stackedWidget.setCurrentIndex(1)

    def abrirPaginaActualizar(self):
        self.ventanaControlarStock.stackedWidget.setCurrentIndex(2)

    def abrirPaginaEliminar(self):
        self.ventanaControlarStock.stackedWidget.setCurrentIndex(3)

    def abrirPaginaInicio(self):

        #AQUI SE AGREGA EL CODIGO PARA VOLVER A LA PAGINA DE MENU OPCIONES
        from menuOpciones import MenuOpciones

        self.hide()  # Oculta la ventana actual de MenuOpciones
        self.menu_window = MenuOpciones()
        self.menu_window.showMenuOpciones()  # Muestra la ventana de login

    # AQUI SE AGREGA LAS FUNCIONES PARA HACERLOS CON LA BASE DE DATOS

    def refrescarBaseDatos(self):

        datos = self.baseDatos.mostrarProductos()
        self.tablaProductos.setRowCount(len(datos))

        for row, producto in enumerate(datos):
            for col, valor in enumerate(producto[0:]):
                self.tablaProductos.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))

    def agregarProducto(self):
        id_producto = self.ventanaControlarStock.lineEditAgregarId.text()
        nombre = self.ventanaControlarStock.lineEditAgregarNombre.text()
        descripcion = self.ventanaControlarStock.lineEditAgregarDescripcion.text()
        precio = self.ventanaControlarStock.lineEditAgregarPrecio.text()
        cantidad_stock = self.ventanaControlarStock.lineEditAgregarCantidadStock.text()
        categoria = self.ventanaControlarStock.lineEditAgregarCategoria.text()

        agregarProductoaBD = self.baseDatos.agregarProductoControlarStock(id_producto, nombre, descripcion, precio, cantidad_stock, categoria)

        self.ventanaControlarStock.lineEditAgregarId.setText("")
        self.ventanaControlarStock.lineEditAgregarNombre.setText("")
        self.ventanaControlarStock.lineEditAgregarDescripcion.setText("")
        self.ventanaControlarStock.lineEditAgregarPrecio.setText("")
        self.ventanaControlarStock.lineEditAgregarCantidadStock.setText("")
        self.ventanaControlarStock.lineEditAgregarCategoria.setText("")

        if agregarProductoaBD:
            print("agregado")
            self.ventanaControlarStock.signalAgregar.setText("Producto agregado")

        else:
            print("no agregado")
            self.ventanaControlarStock.signalAgregar.setText("Producto NO agregado")


    def buscarActualizarProducto(self):

        productoBuscar = self.ventanaControlarStock.lineEditBuscarActualizar.text()
        buscarProductoenBD = self.baseDatos.buscarProductoActualizarControlarStock(productoBuscar)

        if len(buscarProductoenBD) == 0:
            self.ventanaControlarStock.signalActualizarProducto.setText("Producto NO encontrado")

        else:
            self.ventanaControlarStock.signalActualizarProducto.setText("Coincidencias encontradas")

            # MOSTRAR RESULTADOS ENCONTRADOS CUANDO SE DA A BOTON BUSCAR
            self.tablaProductosActualizar = self.ventanaControlarStock.tablaProductosActualizar
            self.tablaProductosActualizar.setRowCount(len(buscarProductoenBD))

            for row, producto in enumerate(buscarProductoenBD):
                for col, valor in enumerate(producto[0:]):
                    self.tablaProductosActualizar.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))


    def seleccionarProducto(self, item):
        row = item.row()
        columnas = ['id', 'nombre', 'descripcion', 'precio', 'cantidad_stock', 'categoria']
        for col, campo in enumerate(columnas):
            valor = self.ventanaControlarStock.tablaProductosActualizar.item(row, col).text()
            self.lineEdits[campo].setText(valor)


    def actualizarProducto(self):

        filaSeleccionada = self.ventanaControlarStock.tablaProductosActualizar.currentRow()

        if filaSeleccionada < 0:
            self.ventanaControlarStock.signalActualizarProducto.setText("Por favor seleccione un producto")
            return

        idOriginal = self.ventanaControlarStock.tablaProductosActualizar.item(filaSeleccionada, 0).text()

        # Obtener los nuevos valores de los LineEdit
        nuevo_id = self.lineEdits['id'].text()
        nuevo_nombre = self.lineEdits['nombre'].text()
        nueva_descripcion = self.lineEdits['descripcion'].text()
        nuevo_precio = self.lineEdits['precio'].text()
        nueva_cantidad = self.lineEdits['cantidad_stock'].text()
        nueva_categoria = self.lineEdits['categoria'].text()

        # Verificar que todos los campos tengan valor
        if not all([nuevo_id, nuevo_nombre, nueva_descripcion, nuevo_precio, nueva_cantidad, nueva_categoria]):
            self.ventanaControlarStock.signalActualizarProducto.setText("Por favor complete todos los campos")
            return

        # Determinar si es una actualización de ID o solo de otros campos
        if idOriginal != nuevo_id:
            # Si el ID cambió, crear nuevo registro y eliminar el antiguo
            actualizacion_exitosa = self.baseDatos.actualizarProductoConNuevoId(
                idOriginal,
                nuevo_id,
                nuevo_nombre,
                nueva_descripcion,
                nuevo_precio,
                nueva_cantidad,
                nueva_categoria
            )
        else:
            # Si el ID no cambió, solo actualizar los otros campos
            actualizacion_exitosa = self.baseDatos.actualizarProductoMismoId(
                nuevo_id,
                nuevo_nombre,
                nueva_descripcion,
                nuevo_precio,
                nueva_cantidad,
                nueva_categoria
            )

        if actualizacion_exitosa:
            self.ventanaControlarStock.signalActualizarProducto.setText("Producto actualizado")

            # Limpiar los campos después de actualizar
            for lineEdit in self.lineEdits.values():
                lineEdit.clear()

            # Actualizar la tabla para mostrar los cambios
            #self.buscarActualizarProducto()

            self.ventanaControlarStock.lineEditBuscarActualizar.clear()

            # Limpiar la tabla
            self.ventanaControlarStock.tablaProductosActualizar.setRowCount(0)

        else:
            self.ventanaControlarStock.signalActualizarProducto.setText("Error al actualizar")


    def buscarEliminarProducto(self):

        productoBuscar = self.ventanaControlarStock.lineEditBuscarEliminar.text()
        buscarProductoenBD = self.baseDatos.buscarProductoActualizarControlarStock(productoBuscar)

        if len(buscarProductoenBD) == 0:
            self.ventanaControlarStock.signalEliminar.setText("Producto NO encontrado")

        else:
            self.ventanaControlarStock.signalEliminar.setText("Coincidencias encontradas")

            # MOSTRAR RESULTADOS ENCONTRADOS CUANDO SE DA A BOTON BUSCAR
            self.tablaEliminar.setRowCount(len(buscarProductoenBD))

            for row, producto in enumerate(buscarProductoenBD):
                for col, valor in enumerate(producto[0:]):
                    self.tablaEliminar.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))


    def seleccionarProductoEliminar(self, item):
        fila_seleccionada = item.row()
        print(fila_seleccionada)
        id_item = self.ventanaControlarStock.tablaEliminar.item(fila_seleccionada, 0)
        print(id_item)

        if id_item is not None:
            # Obtiene el texto del ítem, que es el ID del producto
            id_producto = id_item.text()
            print(f"ID del producto seleccionado: {id_producto}")  # Para depuración

            # Guarda el ID del producto como un atributo de la clase
            self.id_producto_seleccionado = id_producto

            # Actualiza la señal en la interfaz
            self.ventanaControlarStock.signalEliminar.setText(f"Producto seleccionado: {id_producto}")

            # Habilita el botón de eliminar
            self.ventanaControlarStock.botonEliminarProducto.setEnabled(True)
        else:
            print("No se pudo obtener el ID del producto")
            self.ventanaControlarStock.signalEliminar.setText("Error al seleccionar el producto")
            self.ventanaControlarStock.botonEliminarProducto.setEnabled(False)

    def eliminarProducto(self):
        if not hasattr(self, 'id_producto_seleccionado'):
            self.ventanaControlarStock.signalEliminar.setText("Por favor, seleccione un producto primero")
            return

        try:
            # Intenta eliminar el producto de la base de datos
            if self.baseDatos.eliminarProducto(self.id_producto_seleccionado):
                # Si la eliminación fue exitosa
                self.ventanaControlarStock.signalEliminar.setText(
                    f"Producto {self.id_producto_seleccionado} eliminado con éxito")

                # Limpiar la tabla
                self.ventanaControlarStock.tablaEliminar.setRowCount(0)

                # Limpia la selección y deshabilita el botón de eliminar
                delattr(self, 'id_producto_seleccionado')
                self.ventanaControlarStock.botonEliminarProducto.setEnabled(False)

                # Limpiar el campo de búsqueda
                self.ventanaControlarStock.lineEditBuscarEliminar.clear()

            else:
                # Si hubo un problema al eliminar
                self.ventanaControlarStock.signalEliminar.setText("Error al eliminar el producto de la base de datos")

        except Exception as e:
            # Si ocurre cualquier otro error
            print(f"Error inesperado: {e}")
            self.ventanaControlarStock.signalEliminar.setText("Error inesperado al eliminar el producto")

        print("Operación de eliminación completada")  # Para depuración



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    menu = ControlarStock()
    menu.show()
    app.exec_()