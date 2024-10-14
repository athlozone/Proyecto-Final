from PyQt5 import QtWidgets, uic

class RegistrarCompras(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ventanaRegistrarCompras = uic.loadUi('ventanaRegistrarCompras/ventanaRegistrarCompras.ui', self)

        self.ventanaRegistrarCompras.botonBaseDatos.clicked.connect(self.abrirPaginaBaseDatos)

        self.ventanaRegistrarCompras.botonAgregar.clicked.connect(self.abrirPaginaAgregar)
        self.ventanaRegistrarCompras.botonAgregarDetalles.clicked.connect(self.abrirPaginaAgregarDetalleCompra)

        self.ventanaRegistrarCompras.botonActualizar.clicked.connect(self.abrirPaginaActualizar)
        self.ventanaRegistrarCompras.botonActualizarDetalles.clicked.connect(self.abrirPaginaActualizarDetalleCompra)

        self.ventanaRegistrarCompras.botonEliminar.clicked.connect(self.abrirPaginaEliminar)

        self.ventanaRegistrarCompras.botonVolver.clicked.connect(self.abrirPaginaInicio)



        self.ventanaRegistrarCompras.botonRefrescar.clicked.connect(self.refrescarBaseDatos)

        self.ventanaRegistrarCompras.botonAgregarCompra.clicked.connect(self.agregarCompra)
        self.ventanaRegistrarCompras.botonAgregarDetalleCompra.clicked.connect(self.agregarCompraDetalle)
        self.ventanaRegistrarCompras.botonFinalizarDestalleCompra.clicked.connect(self.finalizarCompraDetalle)

        self.ventanaRegistrarCompras.botonBuscarEliminar.clicked.connect(self.buscarEliminarCompra)
        self.ventanaRegistrarCompras.botonEliminarCompra.clicked.connect(self.eliminarCompra)

        self.ventanaRegistrarCompras.botonBuscarActualizarCompra.clicked.connect(self.buscarActualizarCompra)
        self.ventanaRegistrarCompras.botonActualizarDetalle.clicked.connect(self.actualizarDetalleCompra)
        self.ventanaRegistrarCompras.botonActualizarCompra.clicked.connect(self.actualizarCompra)
        self.ventanaRegistrarCompras.botonSalirDetalles.clicked.connect(self.salirDetalleCompra)





    def abrirPaginaBaseDatos(self):
        self.ventanaRegistrarCompras.stackedWidget.setCurrentIndex(0)

    def abrirPaginaAgregar(self):
        self.ventanaRegistrarCompras.stackedWidget.setCurrentIndex(1)


    def abrirPaginaEliminar(self):
        self.ventanaRegistrarCompras.stackedWidget.setCurrentIndex(2)

    def abrirPaginaAgregarDetalleCompra(self):
        self.ventanaRegistrarCompras.stackedWidget.setCurrentIndex(3)

    def abrirPaginaActualizar(self):
        self.ventanaRegistrarCompras.stackedWidget.setCurrentIndex(4)


    def abrirPaginaActualizarDetalleCompra(self):
        self.ventanaRegistrarCompras.stackedWidget.setCurrentIndex(5)

    def abrirPaginaInicio(self):
        from menuOpciones import MenuOpciones

        self.hide()  # Oculta la ventana actual de MenuOpciones
        self.menu_window = MenuOpciones()
        self.menu_window.showMenuOpciones()  # Muestra la ventana de login


    # AQUI SE AGREGA LAS FUNCIONES PARA HACERLOS CON LA BASE DE DATOS

    def refrescarBaseDatos(self):
        print("REFRESCANDO COMPRA")

    def agregarCompra(self):
        print("COMPRA AGREGADO")

    def agregarCompraDetalle(self):
        print("DETALLE COMPRA AGREGADO")

    def finalizarCompraDetalle(self):
        print("COMPRA DETALLE FINALIZADO")

    def buscarActualizarCompra(self):
        print("BUSCANDO PARA ACTUALIZAR COMPRA")

    def actualizarCompra(self):
        print("COMPRA ACTUALIZADO")

    def buscarEliminarCompra(self):
        print("BUSCANDO PARA ELIMINAR COMPRA")


    def eliminarCompra(self):
        print("COMPRA ELIMINADO")


    def actualizarDetalleCompra(self):
        print("DETALLE O PRODUCTO ACTUALIZADO")

    def salirDetalleCompra(self):
        self.ventanaRegistrarCompras.stackedWidget.setCurrentIndex(4)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    menu = RegistrarCompras()
    menu.show()
    app.exec_()
