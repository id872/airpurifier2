#!/usr/bin/env python3.6
import sys

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtCore import QTimer
except ImportError:
    print('PyQt5 is required to run this script')
    sys.exit(1)

try:
    from miio.airpurifier import AirPurifier, OperationMode
    from miio import exceptions as miio_exceptions
except ImportError:
    print('miio is required to run this script')
    sys.exit(1)

from mainwindow import Ui_MainWindow

TOKEN = 'your device token here'
AIR_PUR_IP = '192.168.1.111'


class AirPurifier2App(QMainWindow, Ui_MainWindow):
    def init_device(self) -> AirPurifier or None:
        try:
            return AirPurifier(AIR_PUR_IP, TOKEN)
        except ValueError:
            self.statusbar.showMessage('Invalid TOKEN format', 9999)
            return None

    def init_state_combo(self):
        self.stateComboBox.addItem('Idle (OFF)', OperationMode.Idle)
        self.stateComboBox.addItem('AUTO', OperationMode.Auto)
        self.stateComboBox.addItem('Favorite', OperationMode.Favorite)
        self.stateComboBox.addItem('Sleep', OperationMode.Silent)

    def __init__(self, *args, **kwargs):
        super(AirPurifier2App, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.fav_change = False

        self.dev = self.init_device()
        self.init_state_combo()

        self.check_dev()

        self.stateComboBox.currentIndexChanged.connect(self.set_mode)
        self.favSlider.sliderReleased.connect(self.set_fav_lvl)
        self.favSlider.sliderPressed.connect(self.fav_changing)
        self.favSlider.sliderReleased.connect(self.fav_changed)

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_dev)
        self.timer.start(2500)

    def fav_changing(self):
        self.fav_change = True

    def fav_changed(self):
        self.fav_change = False

    def device_get_status(self) -> AirPurifier.status:
        if self.dev is not None:
            return self.dev.status()

        return None

    def check_response(self, resp: str):
        if 'ok' in resp:
            self.statusbar.showMessage('Response OK', 1000)
        else:
            self.statusbar.showMessage('Response NOK!', 1000)

    def set_mode(self):
        if self.dev is None:
            return

        op_mode = self.stateComboBox.itemData(self.stateComboBox.currentIndex())

        if op_mode == self.device_get_status().mode:
            return

        self.check_response(self.dev.set_mode(op_mode))

    def set_fav_lvl(self):
        if self.dev is None:
            return

        lvl = window.favSlider.value()

        if lvl == self.device_get_status().favorite_level:
            return

        self.check_response(self.dev.set_favorite_level(lvl))

    def check_aqi(self):
        if self.dev is None:
            return

        self.statusbar.showMessage(f'AQI: {self.dev.status().aqi}')

    def check_state(self):
        if self.dev is None:
            return

        dev_mode = self.device_get_status().mode

        idx = self.stateComboBox.findData(dev_mode)

        if idx != self.stateComboBox.currentIndex():
            self.stateComboBox.setCurrentIndex(idx)

    def check_fav_level(self):
        if self.dev is None:
            return

        if not self.fav_change:
            self.favSlider.setValue(self.dev.status().favorite_level)

    def check_dev(self):
        self.check_aqi()
        self.check_state()
        self.check_fav_level()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    try:
        window = AirPurifier2App()
        window.show()
        app.exec_()
    except miio_exceptions.DeviceException as e:
        print(e)
        sys.exit(1)
