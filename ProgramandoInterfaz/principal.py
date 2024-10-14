from PyQt5 import QtWidgets, uic
from menuOpciones import MenuOpciones

class VentanaLogin():

    def __init__(self):

        # INICIAR LA APLICACION
        self.app = QtWidgets.QApplication([])

        # CARGAR ARCHIVOS UI (INTERFAZ GRAFICA)
        self.ventanaLogin = uic.loadUi("ventanaLogin/ventanaLogin1.ui")
        self.ventanaLoginIncorrecto = uic.loadUi("ventanaLogin/ventanaLogin2-inicioIncorrecto.ui")

        # CONEXION DE BOTONES CON FUNCION
        self.ventanaLogin.pushButton.clicked.connect(self.guiVentanaLogin)
        self.ventanaLogin.pushButton_3.clicked.connect(self.salir)

        self.ventanaLoginIncorrecto.pushButton_4.clicked.connect(self.regresardeventanaLoginInCorrecto)
        self.ventanaLoginIncorrecto.pushButton_3.clicked.connect(self.salir)

        self.ejecutarApp()

    # -----------------------------------------------------------------------------------------------------
    # FUNCION OBTENER DATOS DE LOGIN VENTANA LOGIN AQUI SE AGREGARIA LA CONEXION CON LA BASE DE DATOS
    def guiVentanaLogin(self):

        name = self.ventanaLogin.lineEdit.text()
        password = self.ventanaLogin.lineEdit_2.text()

        # AQUI SE DEB PONER EL CODIGO QUE EVALUE EN LA BASE DE DATOS LA CONTRASEÑA Y EL USUARIO
        #Y DEPENDIENDO DEL ROL SI ES ADMIN MUESTRE ESTA INTERFAZ Y SI ES VENDEDOR QUE MUESTRE LA INTERFAZ DE VENDEDOR

        if len(name) == 0 or len(password) == 0:
            self.ventanaLogin.label_4.setText("Ingrese todos los datos")

        elif name == "jose" and password == "jose":
            self.ventanaLogin.hide()
            MenuOpciones().showMenuOpciones()

        else:
            self.ventanaLogin.hide()
            self.guiventanaLoginIncorrecto()

    # FUNCION MOSTRAR VENTANA LOGIN INCORRECTO
    def guiventanaLoginIncorrecto(self):
        self.ventanaLogin.hide()
        self.ventanaLoginIncorrecto.show()

    # FUNCION BOTON REGRESAR DESDE LA VENTA DE INICIO DE SESION CORRECTO
    def regresardeventanaMenuOpciones(self):
        MenuOpciones().hideMenuOpciones()

        # LIMPIAR CAMPO DE USUARIO Y CONTRASEÑA
        name = self.ventanaLogin.lineEdit
        password = self.ventanaLogin.lineEdit_2
        name.setText("")
        password.setText("")

        # LIMPIAR CAMPO DE INGRESE TODOS LOS DATOS
        self.ventanaLogin.label_4.setText("")

        self.ventanaLogin.show()

    # FUNCION BOTON REGRESAR DESDE LA VENTA DE INICIO DE SESION INCORRECTO
    def regresardeventanaLoginInCorrecto(self):
        self.ventanaLoginIncorrecto.hide()

        # LIMPIAR CAMPO DE USUARIO Y CONTRASEÑA
        name = self.ventanaLogin.lineEdit
        password = self.ventanaLogin.lineEdit_2
        name.setText("")
        password.setText("")

        # LIMPIAR CAMPO DE INGRESE TODOS LOS DATOS
        self.ventanaLogin.label_4.setText("")

        self.ventanaLogin.show()

    # FUNCION BOTON SALIR DEL PROGRAMA
    def salir(self):
        self.app.exit()

    def conectarBotones(self):
        # CONEXION DE BOTONES CON FUNCION
        self.ventanaLogin.pushButton.clicked.connect(self.guiVentanaLogin)
        self.ventanaLogin.pushButton_3.clicked.connect(self.salir)

        self.ventanaLoginIncorrecto.pushButton_4.clicked.connect(self.regresardeventanaLoginInCorrecto)
        self.ventanaLoginIncorrecto.pushButton_3.clicked.connect(self.salir)

    def ejecutarApp(self):

        # EJECUTAR APP
        self.ventanaLogin.show()
        self.app.exec_()


# Asegúrate de incluir el bloque principal para ejecutar la ventana
if __name__ == "__main__":
    login = VentanaLogin()  # Instanciar la clase VentanaLogin
