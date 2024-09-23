from PyQt5 import QtWidgets, uic

class MenuOpciones(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventanaMenuOpciones = uic.loadUi("ventanaMenuOpciones/ventanaMenuOpciones.ui", self)

    def showMenuOpciones(self):
        self.show()

    def hideMenuOpciones(self):
        self.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    menu = MenuOpciones()
    menu.show()
    app.exec_()