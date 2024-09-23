from PyQt5 import QtWidgets, uic

# INICIAR LA APLICACION
app = QtWidgets.QApplication([])

# CARGAR ARCHIVOS UI (INTERFAZ GRAFICA)
ventanaLogin = uic.loadUi("ventanaLogin/ventanaLogin1.ui")
ventanaLoginIncorrecto = uic.loadUi("ventanaLogin/ventanaLogin2-inicioIncorrecto.ui")
ventanaMenuOpciones = uic.loadUi("ventanaMenuOpciones/ventanaMenuOpciones.ui")
ventanaControlarStock = uic.loadUi("ventanaControlarStock/ventanaControlarStock.ui")
ventanaGestionarProveedores = uic.loadUi("ventanaGestionarProveedores/ventanaGestionarProveedores.ui")
ventanaGestionarClientes = uic.loadUi("ventanaGestionarClientes/ventanaGestionarClientes.ui")
ventanaRegistrarCompras = uic.loadUi("ventanaRegistrarCompras/ventanaRegistrarCompras.ui")
ventanaRealizarVentas = uic.loadUi("ventanaRealizarVentas/ventanaRealizarVentas.ui")


# -----------------------------------------------------------------------------------------------------
# FUNCION OBTENER DATOS DE LOGIN VENTANA LOGIN AQUI SE AGREGARIA LA CONEXION CON LA BASE DE DATOS
def guiVentanaLogin():

    name = ventanaLogin.lineEdit.text()
    password = ventanaLogin.lineEdit_2.text()

    if len(name) == 0 or len(password) == 0:
        ventanaLogin.label_4.setText("Ingrese todos los datos")

    elif name == "jose" and password == "jose123":
        guiventanaMenuOpciones()

    else:
        guiventanaLoginIncorrecto()

# -----------------------------------------------------------------------------------------------------

# FUNCION MOSTRAR VENTANA LOGIN CORRECTO
def guiventanaMenuOpciones():
    ventanaLogin.hide()
    ventanaMenuOpciones.show()

# FUNCION MOSTRAR VENTANA LOGIN INCORRECTO
def guiventanaLoginIncorrecto():
    ventanaLogin.hide()
    ventanaLoginIncorrecto.show()

# FUNCION BOTON REGRESAR DESDE LA VENTA DE INICIO DE SESION CORRECTO
def regresardeventanaMenuOpciones():
    ventanaMenuOpciones.hide()

    # LIMPIAR CAMPO DE USUARIO Y CONTRASEÑA
    name = ventanaLogin.lineEdit
    password = ventanaLogin.lineEdit_2
    name.setText("")
    password.setText("")

    # LIMPIAR CAMPO DE INGRESE TODOS LOS DATOS
    ventanaLogin.label_4.setText("")

    ventanaLogin.show()

# FUNCION BOTON REGRESAR DESDE LA VENTA DE INICIO DE SESION INCORRECTO
def regresardeventanaLoginInCorrecto():
    ventanaLoginIncorrecto.hide()

    # LIMPIAR CAMPO DE USUARIO Y CONTRASEÑA
    name = ventanaLogin.lineEdit
    password = ventanaLogin.lineEdit_2
    name.setText("")
    password.setText("")

    # LIMPIAR CAMPO DE INGRESE TODOS LOS DATOS
    ventanaLogin.label_4.setText("")

    ventanaLogin.show()

# FUNCION BOTON SALIR DEL PROGRAMA
def salir():
    app.exit()


# FUNCION CONTROLAR STOCK
def controlarStock():
    ventanaMenuOpciones.hide()
    ventanaControlarStock.show()

# FUNCION GESTIONAR PROVEEDORES
def gestionarProveedores():
    ventanaMenuOpciones.hide()
    ventanaGestionarProveedores.show()

# FUNCION GESTIONAR CLIENTES
def gestionarClientes():
    ventanaMenuOpciones.hide()
    ventanaGestionarClientes.show()

# FUNCION REGISTRAR COMPRAS
def registrarCompras():
    ventanaMenuOpciones.hide()
    ventanaRegistrarCompras.show()

# FUNCION REALIZAR VENTAS
def realizarVentas():
    ventanaMenuOpciones.hide()
    ventanaRealizarVentas.show()



# CONEXION DE BOTONES CON FUNCION
ventanaLogin.pushButton.clicked.connect(guiVentanaLogin)
ventanaLogin.pushButton_3.clicked.connect(salir)

ventanaMenuOpciones.pushButton_4.clicked.connect(regresardeventanaMenuOpciones)
ventanaMenuOpciones.pushButton_3.clicked.connect(salir)
ventanaMenuOpciones.botonControlarStock.clicked.connect(controlarStock)
ventanaMenuOpciones.botonGestionarProveedores.clicked.connect(gestionarProveedores)
ventanaMenuOpciones.botonGestionarClientes.clicked.connect(gestionarClientes)
ventanaMenuOpciones.botonRealizarVentas.clicked.connect(realizarVentas)
ventanaMenuOpciones.botonRegistrarCompras.clicked.connect(registrarCompras)

ventanaLoginIncorrecto.pushButton_4.clicked.connect(regresardeventanaLoginInCorrecto)
ventanaLoginIncorrecto.pushButton_3.clicked.connect(salir)


# EJECUTAR APP
ventanaLogin.show()
app.exec()
