import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from plyer import notification
notification.notify(message = 'Программа выполнена успешно', app_name = 'script', title='Готово')

class TestTimer(QWidget):

    def __init__(self):
        super().__init__()

        timer = QTimer(self)
        timer.timeout.connect(self.updtTime)

        self.testTimeDisplay = QLCDNumber(self)
        self.testTimeDisplay.setSegmentStyle(QLCDNumber.Filled)
        self.testTimeDisplay.setDigitCount(8)

        self.label = QLabel("Укажите время для оповещения в формате:  ЧЧ:MM:CC")

        self.lineEdit = QLineEdit(placeholderText="Укажите время для оповещения в формате:  ЧЧ:MM:CC")
        self.lineEdit.setInputMask('99:99:99')

        # чтобы продемонстрировать работу пока вы думаете:
        currentTime = QDateTime.currentDateTime().toString('hh:mm:ss')[:6] + '59'
        self.lineEdit.setText(currentTime)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.testTimeDisplay)
        vbox.addWidget(self.label)
        vbox.addWidget(self.lineEdit)

        self.updtTime()
        timer.start(1000)

    def updtTime(self):
        currentTime = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.testTimeDisplay.display(currentTime)

        if currentTime == self.lineEdit.text():
            self.flashSplash()


    def flashSplash(self):
        # Обязательно сохраните ссылку на SplashScreen иначе это будет мусор
        self.splash = QSplashScreen(QPixmap('C:\\Users\\Rainscar\\Desktop\\12.png').scaled(350, 350, Qt.KeepAspectRatio))

        # По умолчанию SplashScreen будет находиться в центре экрана.
        # Вы можете переместить его в определенное место, если хотите:
        # self.splash.move(10,10)

        self.splash.show()

        # Закройте SplashScreen через 5 секунды (5000 мс)
        QTimer.singleShot(5000, self.splash.close)


if name == '__main__':
    app  = QApplication(sys.argv)
    w = TestTimer()
    w.show()
    w.setWindowTitle('Cоздание оповещений в определенное время')
    w.resize(430, 170)
    sys.exit(app.exec_())
