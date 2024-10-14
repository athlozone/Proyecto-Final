from PyQt5 import QtWidgets, uic
from conexion import Comunicacion

class RealizarVentas(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ventanaRealizarVentas = uic.loadUi('ventanaRealizarVentas/ventanaRealizarVentas.ui', self)

        self.ventanaRealizarVentas.botonBaseDatos.clicked.connect(self.abrirPaginaBaseDatos)
        self.ventanaRealizarVentas.botonAgregar.clicked.connect(self.abrirPaginaAgregar)
        self.ventanaRealizarVentas.botonEliminar.clicked.connect(self.abrirPaginaEliminar)
        self.ventanaRealizarVentas.botonRealizarVenta.clicked.connect(self.abrirPaginaRealizarVenta)
        self.ventanaRealizarVentas.botonActualizar.clicked.connect(self.abrirPaginaActualizarVenta)
        self.ventanaRealizarVentas.botonActualizarDetallesVenta.clicked.connect(self.abrirPaginaActualizarDetalles)
        self.ventanaRealizarVentas.botonEliminarDetalles.clicked.connect(self.abrirPaginaEliminarDetalles)
        self.ventanaRealizarVentas.botonVolver.clicked.connect(self.abrirPaginaInicio)

        self.ventanaRealizarVentas.botonRefrescar.clicked.connect(self.refrescarBaseDatos)
        self.ventanaRealizarVentas.botonAgregarVenta.clicked.connect(self.agregarVenta)
        self.ventanaRealizarVentas.botonAgregarProductoVenta.clicked.connect(self.agregarProductoVenta)
        self.ventanaRealizarVentas.botonFinalizarVenta.clicked.connect(self.finalizarVenta)

        self.ventanaRealizarVentas.botonBuscarVentaActualizar.clicked.connect(self.buscarActualizarVenta)
        self.ventanaRealizarVentas.botonActualizarVenta.clicked.connect(self.actualizarVenta)
        self.ventanaRealizarVentas.botonBuscarEliminar.clicked.connect(self.buscarEliminarVenta)
        self.ventanaRealizarVentas.botonEliminarVenta.clicked.connect(self.eliminarVenta)

        #
        self.ventanaRealizarVentas.botonActualizarDetalleProducto.clicked.connect(self.actualizarProductoDetalleVenta)
        #
        self.ventanaRealizarVentas.botonActualizarDetalle.clicked.connect(self.actualizarDetalleVenta)
        self.ventanaRealizarVentas.botonSalirDetalle.clicked.connect(self.salirDetalleVenta)
        self.ventanaRealizarVentas.botonVolverEliminarDetalleVenta.clicked.connect(self.salirDetalleVentaEliminar)
        self.ventanaRealizarVentas.botonEliminarProductoDetalleVenta.clicked.connect(self.eliminarProductoDetalle)

        self.ventanaRealizarVentas.tablaActualizarVentas.itemClicked.connect(self.seleccionarActualizarVenta)
        self.ventanaRealizarVentas.tablaActualizarDetallesVenta.itemClicked.connect(self.seleccionarActualizarDetalleVenta)
        self.ventanaRealizarVentas.tablaEliminar.itemClicked.connect(self.seleccionarEliminarVenta)
        self.ventanaRealizarVentas.tablaEliminarProductoDetalleVenta.itemClicked.connect(self.seleccionarEliminarProductoDetalle)

        self.lineEdits = {
            'id': self.ventanaRealizarVentas.lineEditBuscarIdVenta,
            'fecha': self.ventanaRealizarVentas.lineEditBuscarFechaVenta,
            'id_cliente': self.ventanaRealizarVentas.lineEditBuscarIdCliente,
            'total': self.ventanaRealizarVentas.lineEditBuscarTotalVenta,
        }

        self.lineEditsDetalles = {
            'cantidad': self.ventanaRealizarVentas.lineEditCantidadDetalle,
            'precio_unitario': self.ventanaRealizarVentas.lineEditPrecioUnitarioDetalle,
        }

        # LLAMAR ARCHÍVO CONEXION PARA ESTABLECER LA CONEXION CON LA BASE DE DATOS
        self.baseDatos = Comunicacion()
        self.tablaVentas = self.ventanaRealizarVentas.tablaVentas
        self.tablaEliminar = self.ventanaRealizarVentas.tablaEliminar
        self.tablaRealizarVentaProductos = self.ventanaRealizarVentas.tablaRealizarVentaProductos
        self.tablaActualizarVentas = self.ventanaRealizarVentas.tablaActualizarVentas
        self.tablaActualizarDetallesVenta = self.ventanaRealizarVentas.tablaActualizarDetallesVenta
        self.tablaEliminarProductoDetalleVenta = self.ventanaRealizarVentas.tablaEliminarProductoDetalleVenta

        self.refrescarBaseDatos()




    def abrirPaginaBaseDatos(self):
        self.ventanaRealizarVentas.stackedWidget.setCurrentIndex(0)

    def abrirPaginaAgregar(self):
        self.ventanaRealizarVentas.stackedWidget.setCurrentIndex(1)

    def abrirPaginaEliminar(self):
        self.ventanaRealizarVentas.stackedWidget.setCurrentIndex(2)

    def abrirPaginaRealizarVenta(self):
        self.ventanaRealizarVentas.stackedWidget.setCurrentIndex(4)

    def abrirPaginaActualizarVenta(self):
        self.ventanaRealizarVentas.stackedWidget.setCurrentIndex(5)

    def abrirPaginaActualizarDetalles(self):
        self.ventanaRealizarVentas.stackedWidget.setCurrentIndex(6)
        id_venta = self.ventanaRealizarVentas.lineEditBuscarIdVenta.text()
        self.actualizarDetalleVenta(id_venta)

        self.ventanaRealizarVentas.lineEditBuscarIdVenta.setText("")
        self.ventanaRealizarVentas.lineEditBuscarFechaVenta.setText("")
        self.ventanaRealizarVentas.lineEditBuscarIdCliente.setText("")
        self.ventanaRealizarVentas.lineEditBuscarTotalVenta.setText("")

        self.ventanaRealizarVentas.tablaActualizarVentas.setRowCount(0)

    def abrirPaginaEliminarDetalles(self):
        self.ventanaRealizarVentas.stackedWidget.setCurrentIndex(3)
        self.eliminarDetalleVenta()

        self.ventanaRealizarVentas.lineEditBuscarEliminar.clear()
        self.ventanaRealizarVentas.tablaEliminar.setRowCount(0)
        #self.actualizarDetalleVenta(id_venta)

        #self.ventanaRealizarVentas.lineEditBuscarIdVenta.setText("")
        #self.ventanaRealizarVentas.lineEditBuscarFechaVenta.setText("")
        #self.ventanaRealizarVentas.lineEditBuscarIdCliente.setText("")
        #self.ventanaRealizarVentas.lineEditBuscarTotalVenta.setText("")

        #self.ventanaRealizarVentas.tablaActualizarVentas.setRowCount(0)


    def abrirPaginaInicio(self):
        from menuOpciones import MenuOpciones

        self.hide()  # Oculta la ventana actual de MenuOpciones
        self.menu_window = MenuOpciones()
        self.menu_window.showMenuOpciones()  # Muestra la ventana de opciones



    ################################# AQUI SE AGREGAN LAS FUNCIONES PARA HACERLOS CON LA BASE DE DATOS #################################


    def refrescarBaseDatos(self):

        datos = self.baseDatos.mostrarVentas()
        self.tablaVentas.setRowCount(len(datos))

        for row, venta in enumerate(datos):
            for col, valor in enumerate(venta[0:]):
                self.tablaVentas.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))


    def agregarVenta(self):

        id_venta = self.ventanaRealizarVentas.lineEditAgregarIdVenta.text()
        fecha = self.ventanaRealizarVentas.lineEditAgregarFechaVenta.text()
        id_clientes = self.ventanaRealizarVentas.lineEditAgregarIdCliente.text()
        total = self.ventanaRealizarVentas.lineEditAgregarValorVenta.text()


        agregarVentaBD = self.baseDatos.agregarVenta(id_venta, fecha, id_clientes, total)

        self.ventanaRealizarVentas.lineEditAgregarIdVenta.setText("")
        self.ventanaRealizarVentas.lineEditAgregarFechaVenta.setText("")
        self.ventanaRealizarVentas.lineEditAgregarIdCliente.setText("")
        self.ventanaRealizarVentas.lineEditAgregarValorVenta.setText("")

        if agregarVentaBD:
            print("agregado")
            self.ventanaRealizarVentas.signalAgregar.setText("Venta agregada")

        else:
            print("no agregado")
            self.ventanaRealizarVentas.signalAgregar.setText("Venta NO agregado)")


    def refrescarBaseDatosDetallesVenta(self, idVenta):

        totalVenta = 0
        datos = self.baseDatos.mostrarDetallesVentas(idVenta)
        self.tablaRealizarVentaProductos.setRowCount(len(datos))

        for row, detalle in enumerate(datos):
            totalVenta += int(detalle[2] * detalle[3])
            for col, valor in enumerate(detalle[0:]):
                self.tablaRealizarVentaProductos.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))

        self.ventanaRealizarVentas.signalTotalVenta.setText(str(totalVenta))


    def agregarProductoVenta(self):

        id_venta = self.ventanaRealizarVentas.lineEditIdVentaRealizarVenta.text()
        id_producto = self.ventanaRealizarVentas.lineEditIdProductoRealizarVenta.text()
        cantidad = self.ventanaRealizarVentas.lineEditCantidadRealizarVenta.text()
        precio_unitario = self.ventanaRealizarVentas.lineEditPrecioUnitarioRealizarVenta.text()

        agregarProductoVentaBD = self.baseDatos.agregarProductoVenta(id_venta, id_producto, cantidad, precio_unitario)

        self.ventanaRealizarVentas.lineEditIdVentaRealizarVenta.setText("")
        self.ventanaRealizarVentas.lineEditIdProductoRealizarVenta.setText("")
        self.ventanaRealizarVentas.lineEditCantidadRealizarVenta.setText("")
        self.ventanaRealizarVentas.lineEditPrecioUnitarioRealizarVenta.setText("")

        if agregarProductoVentaBD:
            print("agregado")
            self.ventanaRealizarVentas.signalAgregar.setText("producto a venta agregada")

        else:
            print("no agregado")
            self.ventanaRealizarVentas.signalAgregar.setText("producto a venta NO agregado)")

        self.refrescarBaseDatosDetallesVenta(id_venta)


    def finalizarVenta(self):

        id_venta = self.tablaRealizarVentaProductos.item(0, 0).text()
        fecha = self.ventanaRealizarVentas.lineEditIdVentaRealizarVentaFecha.text()
        id_clientes = self.ventanaRealizarVentas.lineEditIdVentaRealizarVentaIdCliente.text()
        total = self.ventanaRealizarVentas.signalTotalVenta.text()
        print(id_venta)
        print(fecha)
        print(id_clientes)
        print(total)

        agregarVentaBD = self.baseDatos.agregarVenta(id_venta, fecha, id_clientes, total)

        self.ventanaRealizarVentas.lineEditIdVentaRealizarVenta.setText("")
        self.ventanaRealizarVentas.lineEditIdProductoRealizarVenta.setText("")
        self.ventanaRealizarVentas.lineEditCantidadRealizarVenta.setText("")
        self.ventanaRealizarVentas.lineEditPrecioUnitarioRealizarVenta.setText("")
        self.ventanaRealizarVentas.lineEditIdVentaRealizarVentaFecha.setText("")
        self.ventanaRealizarVentas.lineEditIdVentaRealizarVentaIdCliente.setText("")

        if agregarVentaBD:
            print("agregado")
            self.ventanaRealizarVentas.signalAgregar.setText("Venta agregada")

        else:
            print("no agregado")
            self.ventanaRealizarVentas.signalAgregar.setText("Venta NO agregado)")


    def buscarActualizarVenta(self):

        ventaBuscar = self.ventanaRealizarVentas.lineEditBuscarVentaActualizar.text()
        buscaVentaBD = self.baseDatos.buscarVentaActualizar(ventaBuscar)
        self.ventanaRealizarVentas.lineEditBuscarVentaActualizar.clear()

        if len(buscaVentaBD) == 0:
            self.ventanaRealizarVentas.signalVentaActualizada.setText("Cliente NO encontrado")

        else:
            self.ventanaRealizarVentas.signalVentaActualizada.setText("Coincidencias encontradas")

            # MOSTRAR RESULTADOS ENCONTRADOS CUANDO SE DA A BOTON BUSCAR
            self.tablaActualizarVentas.setRowCount(len(buscaVentaBD))

            for row, venta in enumerate(buscaVentaBD):
                for col, valor in enumerate(venta[0:]):
                    self.tablaActualizarVentas.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))


    def seleccionarActualizarVenta(self, item):
        row = item.row()
        columnas = ['id', 'fecha', 'id_cliente', 'total']
        for col, campo in enumerate(columnas):
            valor = self.ventanaRealizarVentas.tablaActualizarVentas.item(row, col).text()
            self.lineEdits[campo].setText(valor)


    def actualizarVenta(self):
        filaSeleccionada = self.ventanaRealizarVentas.tablaActualizarVentas.currentRow()

        if filaSeleccionada < 0:
            self.ventanaRealizarVentas.signalVentaActualizada.setText("Por favor seleccione una venta")
            return

        idOriginal = self.ventanaRealizarVentas.tablaActualizarVentas.item(filaSeleccionada, 0).text()

        # Obtener los nuevos valores de los LineEdit
        nuevo_id = self.lineEdits['id'].text()
        nueva_fecha = self.lineEdits['fecha'].text()
        nuevo_id_cliente = self.lineEdits['id_cliente'].text()
        nuevo_total = self.lineEdits['total'].text()


        # Verificar que todos los campos tengan valor
        if not all([nuevo_id, nueva_fecha, nuevo_id_cliente, nuevo_total]):
            self.ventanaRealizarVentas.signalVentaActualizada.setText("Por favor complete todos los campos")
            return

        # Determinar si es una actualización de ID o solo de otros campos
        if idOriginal != nuevo_id:
            # Si el ID cambió, crear nuevo registro y eliminar el antiguo
            actualizacion_exitosa = self.baseDatos.actualizarVentaConNuevoId(idOriginal, nuevo_id, nueva_fecha, nuevo_id_cliente, nuevo_total)
        else:
            # Si el ID no cambió, solo actualizar los otros campos
            actualizacion_exitosa = self.baseDatos.actualizarVentaMismoId(idOriginal, nuevo_id, nueva_fecha, nuevo_id_cliente, nuevo_total)

        if actualizacion_exitosa:
            self.ventanaRealizarVentas.signalVentaActualizada.setText("Venta actualizado")

            # Limpiar los campos después de actualizar
            for lineEdit in self.lineEdits.values():
                lineEdit.clear()

            self.ventanaRealizarVentas.lineEditBuscarVentaActualizar.clear()

            # Limpiar la tabla
            self.ventanaRealizarVentas.tablaActualizarVentas.setRowCount(0)

        else:
            self.ventanaRealizarVentas.signalVentaActualizada.setText("Error al actualizar")


    def actualizarDetalleVenta(self, id_venta):


        if id_venta == False:
            self.ventanaRealizarVentas.signalDetalleActualizado.setText("Seleccione una venta para actualizar los detalles")

        else:
            self.ventanaRealizarVentas.signalDetalleActualizado.setText(f"Actualizando detalles venta id = {id_venta}")
            datos = self.baseDatos.mostrarDetallesVentas(id_venta)
            totalVenta = 0
            self.tablaActualizarDetallesVenta.setRowCount(len(datos))

            for row, detalle in enumerate(datos):
                totalVenta += int(detalle[2] * detalle[3])
                for col, valor in enumerate(detalle[0:]):
                    self.tablaActualizarDetallesVenta.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))

            self.ventanaRealizarVentas.signalTotalVentaDetalles.setText(str(totalVenta))
            self.refrescarBaseDatosDetallesVenta(id_venta)
            datos = self.baseDatos.actualizarVentaDespuesDeDetalles(id_venta,totalVenta)
            print(totalVenta)
            print("AQUIIIIIIIIIIII")


    def seleccionarActualizarDetalleVenta(self, item):
        row = item.row()
        columnas = ['cantidad', 'precio_unitario']
        for col, campo in enumerate(columnas, start=2):
            valor = self.ventanaRealizarVentas.tablaActualizarDetallesVenta.item(row, col).text()
            self.lineEditsDetalles[campo].setText(valor)


    def actualizarProductoDetalleVenta(self):

        print("111111111111111111111111111111111")
        filaSeleccionada = self.ventanaRealizarVentas.tablaActualizarDetallesVenta.currentRow()

        if filaSeleccionada < 0:
            self.ventanaRealizarVentas.signalDetalleActualizado.setText("Por favor seleccione un producto")
            return

        idVentaOriginal = self.ventanaRealizarVentas.tablaActualizarDetallesVenta.item(filaSeleccionada, 0).text()
        idProductoOriginal = self.ventanaRealizarVentas.tablaActualizarDetallesVenta.item(filaSeleccionada, 1).text()

        # Obtener los nuevos valores de los LineEdit
        nueva_cantidad = self.lineEditsDetalles['cantidad'].text()
        nuevo_precio_unitario = self.lineEditsDetalles['precio_unitario'].text()

        # Verificar que todos los campos tengan valor
        if not all([nueva_cantidad, nuevo_precio_unitario]):
            self.ventanaRealizarVentas.signalDetalleActualizado.setText("Por favor complete todos los campos")
            return

        else:
            # Si el ID no cambió, solo actualizar los otros campos
            actualizacion_exitosa = self.baseDatos.actualizarProductoDetalleVentaMismoId(idVentaOriginal,idProductoOriginal, nueva_cantidad, nuevo_precio_unitario)

        if actualizacion_exitosa:
            self.ventanaRealizarVentas.signalDetalleActualizado.setText("Producto de detalle actualizado")

            # Limpiar los campos después de actualizar
            for lineEdit in self.lineEditsDetalles.values():
                lineEdit.clear()

            #self.ventanaRealizarVentas.lineEditBuscarVentaActualizar.clear()

            # Limpiar la tabla
            self.ventanaRealizarVentas.tablaActualizarVentas.setRowCount(0)

        else:
            self.ventanaRealizarVentas.signalDetalleActualizado.setText("Error al actualizar")

        datos = self.baseDatos.mostrarDetallesVentas(idVentaOriginal)
        totalVenta = 0
        self.tablaActualizarDetallesVenta.setRowCount(len(datos))

        for row, detalle in enumerate(datos):
            totalVenta += int(detalle[2] * detalle[3])
            for col, valor in enumerate(detalle[0:]):
                self.tablaActualizarDetallesVenta.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))

        self.ventanaRealizarVentas.signalTotalVentaDetalles.setText(str(totalVenta))
        self.refrescarBaseDatosDetallesVenta(idVentaOriginal)
        self.actualizarDetalleVenta(idVentaOriginal)
        self.refrescarBaseDatos()


    def buscarEliminarVenta(self):

        ventaBuscar = self.ventanaRealizarVentas.lineEditBuscarEliminar.text()
        buscarVentaenBD = self.baseDatos.buscarVentaActualizar(ventaBuscar)

        if len(buscarVentaenBD) == 0:
            self.ventanaRealizarVentas.signalEliminar.setText("Venta NO encontrado")

        else:
            self.ventanaRealizarVentas.signalEliminar.setText("Coincidencias encontradas")

            # MOSTRAR RESULTADOS ENCONTRADOS CUANDO SE DA A BOTON BUSCAR
            self.tablaEliminar.setRowCount(len(buscarVentaenBD))

            for row, venta in enumerate(buscarVentaenBD):
                for col, valor in enumerate(venta[0:]):
                    self.tablaEliminar.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))


    def seleccionarEliminarVenta(self, item):
        fila_seleccionada = item.row()
        id_item = self.ventanaRealizarVentas.tablaEliminar.item(fila_seleccionada, 0)

        if id_item is not None:
            id_venta = id_item.text()
            print(f"ID de la venta seleccionada: {id_venta}")  # Para depuración

            self.id_venta_seleccionada = id_venta

            self.ventanaRealizarVentas.signalEliminar.setText(f"Venta seleccionada: {id_venta}")
            self.ventanaRealizarVentas.botonEliminarVenta.setEnabled(True)
        else:
            print("No se pudo obtener el ID de la venta")
            self.ventanaRealizarVentas.signalEliminar.setText("Error al seleccionar la venta")
            self.ventanaRealizarVentas.botonEliminarVenta.setEnabled(False)


    def eliminarVenta(self):

        if not hasattr(self, 'id_venta_seleccionada'):
            self.ventanaRealizarVentas.signalEliminar.setText("Por favor, seleccione una venta primero")
            return

        try:
            if self.baseDatos.eliminarVenta(self.id_venta_seleccionada):
                self.ventanaRealizarVentas.signalEliminar.setText(
                    f"Venta {self.id_venta_seleccionada} eliminada con éxito")

                self.ventanaRealizarVentas.tablaEliminar.setRowCount(0)
                delattr(self, 'id_venta_seleccionada')
                self.ventanaRealizarVentas.botonEliminarVenta.setEnabled(False)
                self.ventanaRealizarVentas.lineEditBuscarEliminar.clear()
            else:
                self.ventanaRealizarVentas.signalEliminar.setText("Error al eliminar la venta")

        except Exception as e:
            print(f"Error inesperado: {e}")
            self.ventanaRealizarVentas.signalEliminar.setText("Error inesperado al eliminar la venta")

        print("Operación de eliminación completada")  # Para depuración


    def eliminarDetalleVenta(self):

        idVenta = self.id_venta_seleccionada
        totalVenta = 0
        datos = self.baseDatos.mostrarDetallesVentas(idVenta)
        self.tablaEliminarProductoDetalleVenta.setRowCount(len(datos))

        for row, detalle in enumerate(datos):
            totalVenta += int(detalle[2] * detalle[3])
            for col, valor in enumerate(detalle[0:]):
                self.tablaEliminarProductoDetalleVenta.setItem(row, col, QtWidgets.QTableWidgetItem(str(valor)))

        self.ventanaRealizarVentas.signalTotalVentaEliminar.setText(str(totalVenta))
        self.refrescarBaseDatos()



    def seleccionarEliminarProductoDetalle(self, item):

        fila_seleccionada = item.row()
        self.idVentaEliminar = self.ventanaRealizarVentas.tablaEliminarProductoDetalleVenta.item(fila_seleccionada, 0).text()
        self.idProductoEliminar = self.ventanaRealizarVentas.tablaEliminarProductoDetalleVenta.item(fila_seleccionada, 1).text()
        self.cantidadProductoEliminar = self.ventanaRealizarVentas.tablaEliminarProductoDetalleVenta.item(fila_seleccionada, 2).text()
        self.precioUniProductoEliminar = self.ventanaRealizarVentas.tablaEliminarProductoDetalleVenta.item(fila_seleccionada, 3).text()


        if self.idVentaEliminar is not None:
            print(self.idVentaEliminar)
            print(self.idProductoEliminar)
            print(self.cantidadProductoEliminar)
            print(self.precioUniProductoEliminar)


        else:
            print("No se pudo obtener el ID de la venta")
            self.ventanaRealizarVentas.signalProductoEliminar.setText("Error al seleccionar la venta")
            self.ventanaRealizarVentas.botonEliminarProductoDetalleVenta.setEnabled(False)


    def eliminarProductoDetalle(self):

        datos = self.baseDatos.eliminarProductoVentaDetalle(self.idVentaEliminar, self.idProductoEliminar, self.cantidadProductoEliminar, self.precioUniProductoEliminar)

        if datos:
            self.actualizarDetalleVenta(self.idVentaEliminar)
            self.eliminarDetalleVenta()
            print("eliminado")
            self.ventanaRealizarVentas.signalProductoEliminar.setText("Producto eliminado")

        else:
            print("no eliminado")
            self.ventanaRealizarVentas.signalProductoEliminar.setText("Producto NO eliminado)")


    def salirDetalleVenta(self):
        self.ventanaRealizarVentas.stackedWidget.setCurrentIndex(5)


    def salirDetalleVentaEliminar(self):
        self.ventanaRealizarVentas.stackedWidget.setCurrentIndex(2)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    menu = RealizarVentas()
    menu.show()
    app.exec_()