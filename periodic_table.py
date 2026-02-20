import sys
import elements as el
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton,
    QTextEdit, QGridLayout, QLabel
)
from PySide6.QtGui import QFont


class PeriodicTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Periodic Table")
        self.setStyleSheet("background-color: #000000;")

        central = QWidget()
        self.setCentralWidget(central)
        self.layout = QGridLayout(central)
        self.layout.setSpacing(2)
        self.layout.setContentsMargins(6, 6, 6, 6)

        # Info text box
        self.text1 = QTextEdit()
        self.text1.setReadOnly(True)
        self.text1.setFixedWidth(320)
        self.text1.setStyleSheet(
            "background-color: #404040; color: #FFFFFF; "
            "border: 1px solid #555; padding: 4px;"
        )
        self.text1.setFont(QFont("Courier New", 9))
        self.layout.addWidget(self.text1, 1, 19, 60, 10)

        btn_font = QFont("Arial", 7, QFont.Bold)

        def make_btn(text, bg, fg, data):
            btn = QPushButton(text)
            btn.setFont(btn_font)
            btn.setFixedSize(36, 28)
            btn.setStyleSheet(
                f"QPushButton {{ background-color: {bg}; color: {fg};"
                f" border: 1px solid #333; border-radius: 2px; }}"
                f"QPushButton:hover {{ border: 2px solid #ffffff; }}"
            )
            btn.clicked.connect(lambda checked, d=data: self.f(d))
            return btn

        def add(text, row, col, bg, data, fg="#000000"):
            btn = make_btn(text, bg, fg, data)
            self.layout.addWidget(btn, row, col)

        # Period 1
        add("H",  1,  1,  "#B4B4FF", el.H)
        add("He", 1, 18,  "#004080", el.He, fg="#FFFFFF")

        # Period 2
        add("Li", 2,  1,  "#5FFF5F", el.Li)
        add("Be", 2,  2,  "#EB4B4B", el.Be)
        add("B",  2, 13,  "#B4B400", el.B)
        add("C",  2, 14,  "#B4B4FF", el.C)
        add("N",  2, 15,  "#B4B4FF", el.N)
        add("O",  2, 16,  "#B4B4FF", el.O)
        add("F",  2, 17,  "#B4B4FF", el.F)
        add("Ne", 2, 18,  "#004080", el.Ne, fg="#FFFFFF")

        # Period 3
        add("Na", 3,  1,  "#5FFF5F", el.Na)
        add("Mg", 3,  2,  "#EB4B4B", el.Mg)
        add("Al", 3, 13,  "#A0A0A0", el.Al)
        add("Si", 3, 14,  "#B4B400", el.Si)
        add("P",  3, 15,  "#B4B4FF", el.P)
        add("S",  3, 16,  "#B4B4FF", el.S)
        add("Cl", 3, 17,  "#B4B4FF", el.Cl)
        add("Ar", 3, 18,  "#004080", el.Ar, fg="#FFFFFF")

        # Period 4
        add("K",  4,  1,  "#5FFF5F", el.K)
        add("Ca", 4,  2,  "#EB4B4B", el.Ca)
        add("Sc", 4,  3,  "#FFFFB4", el.Sc)
        add("Ti", 4,  4,  "#FFFFB4", el.Ti)
        add("V",  4,  5,  "#FFFFB4", el.V)
        add("Cr", 4,  6,  "#FFFFB4", el.Cr)
        add("Mn", 4,  7,  "#FFFFB4", el.Mn)
        add("Fe", 4,  8,  "#FFFFB4", el.Fe)
        add("Co", 4,  9,  "#FFFFB4", el.Co)
        add("Ni", 4, 10,  "#FFFFB4", el.Ni)
        add("Cu", 4, 11,  "#FFFFB4", el.Cu)
        add("Zn", 4, 12,  "#FFFFB4", el.Zn)
        add("Ga", 4, 13,  "#A0A0A0", el.Ga)
        add("Ge", 4, 14,  "#B4B400", el.Ge)
        add("As", 4, 15,  "#B4B400", el.As)
        add("Se", 4, 16,  "#B4B4FF", el.Se)
        add("Br", 4, 17,  "#B4B4FF", el.Br)
        add("Kr", 4, 18,  "#004080", el.Kr, fg="#FFFFFF")

        # Period 5
        add("Rb", 5,  1,  "#5FFF5F", el.Rb)
        add("Sr", 5,  2,  "#EB4B4B", el.Sr)
        add("Y",  5,  3,  "#FFFFB4", el.Y)
        add("Zr", 5,  4,  "#FFFFB4", el.Zr)
        add("Nb", 5,  5,  "#FFFFB4", el.Nb)
        add("Mo", 5,  6,  "#FFFFB4", el.Mo)
        add("Tc", 5,  7,  "#FFFFB4", el.Tc)
        add("Ru", 5,  8,  "#FFFFB4", el.Ru)
        add("Rh", 5,  9,  "#FFFFB4", el.Rh)
        add("Pd", 5, 10,  "#FFFFB4", el.Pd)
        add("Ag", 5, 11,  "#FFFFB4", el.Ag)
        add("Cd", 5, 12,  "#FFFFB4", el.Cd)
        add("In", 5, 13,  "#A0A0A0", el.In)
        add("Sn", 5, 14,  "#A0A0A0", el.Sn)
        add("Sb", 5, 15,  "#B4B400", el.Sb)
        add("Te", 5, 16,  "#B4B400", el.Te)
        add("I",  5, 17,  "#B4B4FF", el.I)
        add("Xe", 5, 18,  "#004080", el.Xe, fg="#FFFFFF")

        # Period 6
        add("Cs", 6,  1,  "#5FFF5F", el.Cs)
        add("Ba", 6,  2,  "#EB4B4B", el.Ba)
        add("La", 6,  3,  "#FFFF80", el.La)
        add("Hf", 6,  4,  "#FFFFB4", el.Hf)
        add("Ta", 6,  5,  "#FFFFB4", el.Ta)
        add("W",  6,  6,  "#FFFFB4", el.W)
        add("Re", 6,  7,  "#FFFFB4", el.Re)
        add("Os", 6,  8,  "#FFFFB4", el.Os)
        add("Ir", 6,  9,  "#FFFFB4", el.Ir)
        add("Pt", 6, 10,  "#FFFFB4", el.Pt)
        add("Au", 6, 11,  "#FFFFB4", el.Au)
        add("Hg", 6, 12,  "#FFFFB4", el.Hg)
        add("Tl", 6, 13,  "#A0A0A0", el.Tl)
        add("Pb", 6, 14,  "#A0A0A0", el.Pb)
        add("Bi", 6, 15,  "#A0A0A0", el.Bi)
        add("Po", 6, 16,  "#A0A0A0", el.Po)
        add("At", 6, 17,  "#A0A0A0", el.At)
        add("Rn", 6, 18,  "#004080", el.Rn, fg="#FFFFFF")

        # Period 7
        add("Fr",  7,  1,  "#5FFF5F", el.Fr)
        add("Ra",  7,  2,  "#EB4B4B", el.Ra)
        add("Ac",  7,  3,  "#FFFF80", el.Ac)
        add("Rf",  7,  4,  "#FFFFB4", el.Rf)
        add("Db",  7,  5,  "#FFFFB4", el.Db)
        add("Sg",  7,  6,  "#FFFFB4", el.Sg)
        add("Bh",  7,  7,  "#FFFFB4", el.Bh)
        add("Hs",  7,  8,  "#FFFFB4", el.Hs)
        add("Mt",  7,  9,  "#FFFFB4", el.Mt)
        add("Ds",  7, 10,  "#FFFFB4", el.Ds)
        add("Rg",  7, 11,  "#FFFFB4", el.Rg)
        add("Cn",  7, 12,  "#FFFFB4", el.Cn)
        add("Nh",  7, 13,  "#B1FF64", el.Nh)
        add("Fl",  7, 14,  "#B1FF64", el.Fl)
        add("Mc",  7, 15,  "#B1FF64", el.Mc)
        add("Lv",  7, 16,  "#B1FF64", el.Lv)
        add("Ts",  7, 17,  "#B1FF64", el.Ts)
        add("Og",  7, 18,  "#B1FF64", el.Og)

        # Lanthanides (row 9)
        add("Ce", 9,  3,  "#FFFF80", el.Ce)
        add("Pr", 9,  4,  "#FFFF80", el.Pr)
        add("Nd", 9,  5,  "#FFFF80", el.Nd)
        add("Pm", 9,  6,  "#FFFF80", el.Pm)
        add("Sm", 9,  7,  "#FFFF80", el.Sm)
        add("Eu", 9,  8,  "#FFFF80", el.Eu)
        add("Gd", 9,  9,  "#FFFF80", el.Gd)
        add("Tb", 9, 10,  "#FFFF80", el.Tb)
        add("Dy", 9, 11,  "#FFFF80", el.Dy)
        add("Ho", 9, 12,  "#FFFF80", el.Ho)
        add("Er", 9, 13,  "#FFFF80", el.Er)
        add("Tm", 9, 14,  "#FFFF80", el.Tm)
        add("Yb", 9, 15,  "#FFFF80", el.Yb)
        add("Lu", 9, 16,  "#FFFF80", el.Lu)

        # Actinides (row 10)
        add("Th", 10,  3,  "#FFFF80", el.Th)
        add("Pa", 10,  4,  "#FFFF80", el.Pa)
        add("U",  10,  5,  "#FFFF80", el.U)
        add("Np", 10,  6,  "#FFFF80", el.Np)
        add("Pu", 10,  7,  "#FFFF80", el.Pu)
        add("Am", 10,  8,  "#FFFF80", el.Am)
        add("Cm", 10,  9,  "#FFFF80", el.Cm)
        add("Bk", 10, 10,  "#FFFF80", el.Bk)
        add("Cf", 10, 11,  "#FFFF80", el.Cf)
        add("Es", 10, 12,  "#FFFF80", el.Es)
        add("Fm", 10, 13,  "#FFFF80", el.Fm)
        add("Md", 10, 14,  "#FFFF80", el.Md)
        add("No", 10, 15,  "#FFFF80", el.No)
        add("Lr", 10, 16,  "#FFFF80", el.Lr)

        # Spacer between period 7 and lanthanide/actinide rows
        spacer = QLabel("")
        spacer.setFixedHeight(8)
        self.layout.addWidget(spacer, 8, 3, 1, 14)

        self.resize(1000, 480)

    def f(self, data):
        self.text1.setPlainText(str(data))


def main():
    app = QApplication(sys.argv)
    window = PeriodicTable()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
