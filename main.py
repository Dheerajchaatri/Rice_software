from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)
from costing import max_purchase_rate
from database import setup_db

setup_db()

class RiceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("رائس کاسٹنگ سافٹ ویئر")
        self.setGeometry(300, 200, 350, 400)

        layout = QVBoxLayout()

        self.sale = QLineEdit()
        self.sale.setPlaceholderText("سیل ریٹ (Rs/kg)")

        self.profit = QLineEdit()
        self.profit.setPlaceholderText("منافع")

        self.proc = QLineEdit()
        self.proc.setPlaceholderText("پروسیسنگ خرچ")

        self.full = QLineEdit("0.60")
        self.short = QLineEdit("0.15")
        self.b2 = QLineEdit("0.20")
        self.b3 = QLineEdit("0.05")

        btn = QPushButton("MAX خریداری ریٹ نکالیں")
        btn.clicked.connect(self.calculate)

        self.result = QLabel("")

        layout.addWidget(self.sale)
        layout.addWidget(self.profit)
        layout.addWidget(self.proc)
        layout.addWidget(QLabel("Full %"))
        layout.addWidget(self.full)
        layout.addWidget(QLabel("Short %"))
        layout.addWidget(self.short)
        layout.addWidget(QLabel("B2 %"))
        layout.addWidget(self.b2)
        layout.addWidget(QLabel("B3 %"))
        layout.addWidget(self.b3)
        layout.addWidget(btn)
        layout.addWidget(self.result)

        self.setLayout(layout)

    def calculate(self):
        try:
            rate = max_purchase_rate(
                float(self.sale.text()),
                float(self.profit.text()),
                float(self.proc.text()),
                float(self.full.text()),
                float(self.short.text()),
                float(self.b2.text()),
                float(self.b3.text())
            )
            self.result.setText(f"زیادہ سے زیادہ خریداری ریٹ: {rate} Rs/kg")
        except:
            QMessageBox.warning(self, "Error", "درست نمبر درج کریں")

app = QApplication([])
window = RiceApp()
window.show()
app.exec()
