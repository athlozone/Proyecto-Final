from PyQt5 import QtWidgets, uic

class MenuOpciones(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventanaMenuOpciones = uic.loadUi("ventanaMenuOpciones/ventanaMenuOpciones.ui", self)
        #self.ventanaMenuOpcionesVendedor = uic.loadUi("ventanaMenuOpciones/ventanaMenuOpcionesVendedor.ui.ui", self)
        self.ventanaMenuOpciones.botonSalirMenuOpciones.clicked.connect(self.salir)
        self.ventanaMenuOpciones.botonRegresarMenuOpciones.clicked.connect(self.volveraVentanaLogin)
        self.ventanaMenuOpciones.botonControlarStock.clicked.connect(self.irControlarStock)
        self.ventanaMenuOpciones.botonGestionarProveedores.clicked.connect(self.irGestionarProveedores)
        self.ventanaMenuOpciones.botonGestionarClientes.clicked.connect(self.irGestionarClientes)
        self.ventanaMenuOpciones.botonRealizarVentas.clicked.connect(self.irRealizarVentas)
        self.ventanaMenuOpciones.botonRegistrarCompras.clicked.connect(self.irRegistrarCompras)

    def showMenuOpciones(self):
        self.show()

    def hideMenuOpciones(self):
        self.hide()

    def volveraVentanaLogin(self):
        """from principal import VentanaLogin
        self.hide()
        VentanaLogin().regresando()"""
        # Importa VentanaLogin y crea una nueva instancia
        from principal import VentanaLogin

        self.hide()  # Oculta la ventana actual de MenuOpciones

        self.login_window = VentanaLogin()
        self.login_window.ventanaLogin.show()  # Muestra la ventana de login

    def salir(self):
        self.close()

    def irControlarStock(self):

        from controlarStock import ControlarStock

        self.hide()

        self.stock_window = ControlarStock()
        self.stock_window.show()


    def irGestionarProveedores(self):

        from gestionarProveedores import GestionarProveedores

        self.hide()
        self.proveedores_window = GestionarProveedores()
        self.proveedores_window.show()

    def irGestionarClientes(self):

        from gestionarClientes import GestionarClientes

        self.hide()
        self.clientes_window = GestionarClientes()
        self.clientes_window.show()

    def irRealizarVentas(self):

        from realizarVentas import RealizarVentas
        self.hide()
        self.clientes_window = RealizarVentas()
        self.clientes_window.show()

    def irRegistrarCompras(self):

        from registrarCompras import RegistrarCompras

        self.hide()
        self.clientes_window = RegistrarCompras()
        self.clientes_window.show()





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    menu = MenuOpciones()
    menu.show()
    app.exec_()