from PyQt5 import QtWidgets, uic

class ControlarStock:

    # INICIAR LA APLICACION
    app = QtWidgets.QApplication([])

    ventanaControlarStock = uic.loadUi("ventanaControlarStock/ventanaControlarStock.ui")

    # EJECUTAR APP
    ventanaControlarStock.show()
    app.exec()