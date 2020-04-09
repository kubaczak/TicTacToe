import sys

from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QInputDialog, QLineEdit, QMessageBox
from PyQt5 import QtCore
import baza

from gui import Ui_Dialog
from PyQt5.QtCore import Qt
import threading

def bazacl(output):
    x = output
    t = []
    for i in x:
        z = str(i)
        z = z.replace("(", "")
        z = z.replace(")", "")
        z = z.replace(",", "")
        t.append(z)
    return t

class AppWindow(QDialog, QWidget):

    kolej = False
    pob = False
    dane = None
    gracz = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

        self.ui.mainBtn.clicked.connect(self.polacz)
        self.ui.btn1.clicked.connect(self.graj)
        self.ui.btn2.clicked.connect(self.graj)
        self.ui.btn3.clicked.connect(self.graj)
        self.ui.btn4.clicked.connect(self.graj)
        self.ui.btn5.clicked.connect(self.graj)
        self.ui.btn6.clicked.connect(self.graj)
        self.ui.btn7.clicked.connect(self.graj)
        self.ui.btn8.clicked.connect(self.graj)
        self.ui.btn9.clicked.connect(self.graj)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()

    def pobierzdane(self):
        if self.pob:
            dane = baza.pobierz(self.dane[0])
            if dane == self.dane:
                pass
            else:
                for i in range(len(dane)):
                    if dane[i] == self.dane[i]:
                        pass
                    else:
                        zmiana = False
                        if i == 1:
                            self.ui.btn1.setText(dane[1])
                            zmiana = True
                        if i == 2:
                            self.ui.btn2.setText(dane[2])
                            zmiana = True
                        if i == 3:
                            self.ui.btn3.setText(dane[3])
                            zmiana = True
                        if i == 4:
                            self.ui.btn4.setText(dane[4])
                            zmiana = True
                        if i == 5:
                            self.ui.btn5.setText(dane[5])
                            zmiana = True
                        if i == 6:
                            self.ui.btn6.setText(dane[6])
                            zmiana = True
                        if i == 7:
                            self.ui.btn7.setText(dane[7])
                            zmiana = True
                        if i == 8:
                            self.ui.btn8.setText(dane[8])
                            zmiana = True
                        if i == 9:
                            self.ui.btn9.setText(dane[9])
                            zmiana = True
                        if i == 10 or i == 11:
                            if dane[i] == '0' and self.dane[i] == '1':
                                QMessageBox.about(self, "Uwaga!", "Przeciwnik rozłączyl się!")
                            elif dane[i] == '1' and self.dane[i] == '0':
                                QMessageBox.about(self, "Uwaga!", "Przeciwnik połączył się!")
                        if zmiana:
                            self.pob = False
                            self.ui.label.setText("Teraz Twoja kolej!")
                        self.dane = dane
            spr = self.sprawdz()
            if spr == True:
                baza.usun(self.dane[0])
                self.rzl()
                self.ui.label.setText("Remis!")
            elif spr == "X" and self.gracz == 1 or spr == "O" and self.gracz == 2:
                baza.usun(self.dane[0])
                self.rzl()
                self.ui.label.setText("Wygrałeś!")
            elif spr == "X" or spr == "O":
                baza.usun(self.dane[0])
                self.rzl()
                self.ui.label.setText("Wygrywa przeciwnik!")
            else:
                pass


    def polacz(self):
        sender = self.sender()
        if sender.text() == "Połącz":
            id, okPressed = QInputDialog.getText(self, "Połącz", "Wprowadź ID pokoju:", QLineEdit.Normal, "")
            if okPressed and id != "":
                id = id.replace(" ", "_")
                out, gracz = baza.pol(id)
                if out == None:
                    QMessageBox.about(self, "Bląd!", "Pokój jest pełny!")
                else:
                    self.dane = out
                    ##################print(self.dane)
                    self.ui.label.setText("Połączono!")
                    self.ui.mainBtn.setText("Rozłącz")
                    self.gracz = gracz
                    self.ustaw()
            else:
                QMessageBox.about(self, "Bląd!", "Nazwa nie może być pusta!")
        elif sender.text() == "Rozłącz":
            self.rozlacz()


    def setInterval(self, func, time):
        e = threading.Event()
        while not e.wait(time):
            func()

    def ustaw(self):
        if self.dane[1] != 'A':
            self.ui.btn1.setText(self.dane[1])
        if self.dane[2] != 'A':
            self.ui.btn2.setText(self.dane[2])
        if self.dane[3] != 'A':
            self.ui.btn3.setText(self.dane[3])
        if self.dane[4] != 'A':
            self.ui.btn4.setText(self.dane[4])
        if self.dane[5] != 'A':
            self.ui.btn5.setText(self.dane[5])
        if self.dane[6] != 'A':
            self.ui.btn6.setText(self.dane[6])
        if self.dane[7] != 'A':
            self.ui.btn7.setText(self.dane[7])
        if self.dane[8] != 'A':
            self.ui.btn8.setText(self.dane[8])
        if self.dane[9] != 'A':
            self.ui.btn9.setText(self.dane[9])
        if self.dane[12] == 'X' and self.gracz == 1 or self.dane[12] == 'O' and self.gracz == 2:
            self.ui.label.setText("Twoja kolej!")
        elif self.gracz == 1:
            self.pob = True
            self.ui.label.setText("Kolej gracza O")
        elif self.gracz == 2:
            self.pob = True
            self.ui.label.setText("Kolej gracza X")

    def rzl(self):
        self.pob = False
        self.ui.mainBtn.setText("Połącz")
        self.ui.btn1.setText("")
        self.ui.btn2.setText("")
        self.ui.btn3.setText("")
        self.ui.btn4.setText("")
        self.ui.btn5.setText("")
        self.ui.btn6.setText("")
        self.ui.btn7.setText("")
        self.ui.btn8.setText("")
        self.ui.btn9.setText("")
        self.dane = None
        self.gracz = None
        self.kolej = False

    def rozlacz(self):
        baza.rozlacz(self.dane[0], self.gracz)
        self.pob = False
        self.ui.mainBtn.setText("Połącz")
        self.ui.btn1.setText("")
        self.ui.btn2.setText("")
        self.ui.btn3.setText("")
        self.ui.btn4.setText("")
        self.ui.btn5.setText("")
        self.ui.btn6.setText("")
        self.ui.btn7.setText("")
        self.ui.btn8.setText("")
        self.ui.btn9.setText("")
        self.ui.label.setText("")
        self.dane = None
        self.gracz = None
        self.kolej = False

    def graj(self):
        sender = self.sender()
        print(self.dane[12], self.gracz)
        if self.dane[12] == 'X' and self.gracz == 1:
            if sender.text() == "":
                obj = sender.objectName()
                obj = obj.replace("btn", "")
                obj = int(obj)
                if obj == 1:
                    self.ui.btn1.setText('X')
                    self.dane[1] = 'X'
                    baza.updt(self.dane[0], 'x1', 'X', 'O')
                if obj == 2:
                    self.ui.btn2.setText("X")
                    self.dane[2] = 'X'
                    baza.updt(self.dane[0], 'x2', 'X', 'O')
                if obj == 3:
                    self.ui.btn3.setText("X")
                    self.dane[3] = 'X'
                    baza.updt(self.dane[0], 'x3', 'X', 'O')
                if obj == 4:
                    self.ui.btn4.setText("X")
                    self.dane[4] = 'X'
                    baza.updt(self.dane[0], 'x4', 'X', 'O')
                if obj == 5:
                    self.ui.btn5.setText("X")
                    self.dane[5] = 'X'
                    baza.updt(self.dane[0], 'x5', 'X', 'O')
                if obj == 6:
                    self.ui.btn6.setText("X")
                    self.dane[6] = 'X'
                    baza.updt(self.dane[0], 'x6', 'X', 'O')
                if obj == 7:
                    self.ui.btn7.setText("X")
                    self.dane[7] = 'X'
                    baza.updt(self.dane[0], 'x7', 'X', 'O')
                if obj == 8:
                    self.ui.btn8.setText("X")
                    self.dane[8] = 'X'
                    baza.updt(self.dane[0], 'x8', 'X', 'O')
                if obj == 9:
                    self.ui.btn9.setText("X")
                    self.dane[9] = 'X'
                    baza.updt(self.dane[0], 'x9', 'X', 'O')
                self.ui.label.setText("Teraz kolej gracza O")
                self.dane[12] = 'O'
                self.pob = True

        if self.dane[12] == 'O' and self.gracz == 2:
            if sender.text() == "":
                obj = sender.objectName()
                obj = obj.replace("btn", "")
                obj = int(obj)
                if obj == 1:
                    self.ui.btn1.setText("O")
                    self.dane[1] = 'O'
                    baza.updt(self.dane[0], 'x1', 'O', 'X')
                if obj == 2:
                    self.ui.btn2.setText("O")
                    self.dane[2] = 'O'
                    baza.updt(self.dane[0], 'x2', 'O', 'X')
                if obj == 3:
                    self.ui.btn3.setText("O")
                    self.dane[3] = 'O'
                    baza.updt(self.dane[0], 'x3', 'O', 'X')
                if obj == 4:
                    self.ui.btn4.setText("O")
                    self.dane[4] = 'O'
                    baza.updt(self.dane[0], 'x4', 'O', 'X')
                if obj == 5:
                    self.ui.btn5.setText("O")
                    self.dane[5] = 'O'
                    baza.updt(self.dane[0], 'x5', 'O', 'X')
                if obj == 6:
                    self.ui.btn6.setText("O")
                    self.dane[6] = 'O'
                    baza.updt(self.dane[0], 'x6', 'O', 'X')
                if obj == 7:
                    self.ui.btn7.setText("O")
                    self.dane[7] = 'O'
                    baza.updt(self.dane[0], 'x7', 'O', 'X')
                if obj == 8:
                    self.ui.btn8.setText("O")
                    self.dane[8] = 'O'
                    baza.updt(self.dane[0], 'x8', 'O', 'X')
                if obj == 9:
                    self.ui.btn9.setText("O")
                    self.dane[9] = 'O'
                    baza.updt(self.dane[0], 'x9', 'O', 'X')
                self.ui.label.setText("Teraz kolej gracza X")
                self.dane[12] = 'X'
                self.pob = True
        spr = self.sprawdz()
        print(spr)
        if spr == True:
            self.ui.label.setText("Remis!")
            self.rzl()
        elif spr == "X" and self.gracz == 1 or spr == "O" and self.gracz == 2:
            self.ui.label.setText("Wygrałeś!")
            self.rzl()
        elif spr == "X" or spr == "O":
            self.ui.label.setText("Wygrywa przeciwnik!")
            self.rzl()
        else:
            pass

    def sprawdz(self):
        xo = [['A', 'A', 'A'], ['A', 'A', 'A'], ['A', 'A', 'A']]
        xo[0][0] = self.ui.btn1.text()
        xo[0][1] = self.ui.btn2.text()
        xo[0][2] = self.ui.btn3.text()
        xo[1][0] = self.ui.btn4.text()
        xo[1][1] = self.ui.btn5.text()
        xo[1][2] = self.ui.btn6.text()
        xo[2][0] = self.ui.btn7.text()
        xo[2][1] = self.ui.btn8.text()
        xo[2][2] = self.ui.btn9.text()
        for x in range(0, 3):
            if xo[x][0] == "X" and xo[x][1] == "X" and xo[x][2] == "X":
                return 'X'
            elif xo[0][x] == "X" and xo[1][x] == "X" and xo[2][x] == "X":
                return 'X'
            elif xo[0][0] == "X" and xo[1][1] == "X" and xo[2][2] == "X":
                return 'X'
            elif xo[0][2] == "X" and xo[1][1] == "X" and xo[2][0] == "X":
                return 'X'
            elif xo[x][0] == "O" and xo[x][1] == "O" and xo[x][2] == "O":
                return 'O'
            elif xo[0][x] == "O" and xo[1][x] == "O" and xo[2][x] == "O":
                return 'O'
            elif xo[0][0] == "O" and xo[1][1] == "O" and xo[2][2] == "O":
                return 'O'
            elif xo[0][2] == "O" and xo[1][1] == "O" and xo[2][0] == "O":
                return 'O'
        for i in range(0, 3):
            for j in range(0, 3):
                if xo[i][j] == "":
                    return False
        return True

    def closeEvent(self, QCloseEvent):
        if self.dane != None:
            self.rozlacz()
            QCloseEvent.accept()
        else:
            QCloseEvent.accept()



app = QApplication(sys.argv)
w = AppWindow()
w.show()


timer = QtCore.QTimer()
timer.timeout.connect(w.pobierzdane)
timer.setInterval(2000)
timer.start()

sys.exit(app.exec_())
