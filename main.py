import sys, os
from ui_main import Ui_MainWindow

from serial import Serial
import re, json, datetime

from PyQt5 import QtTest, QtWidgets, QtCore


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ser = None
        self.setupUi(self)

        self.pushButton.clicked.connect(self.serial_conn)
        self.pushButton_2.clicked.connect(self.serial_close)
        self.pushButton_10.clicked.connect(self.data_cont)
        self.pushButton_11.clicked.connect(self.data_stop)
        self.pushButton_3.clicked.connect(lambda: self.serial_cmd('N'))
        self.pushButton_4.clicked.connect(lambda: self.serial_cmd('F'))

        self.pushButton_5.clicked.connect(lambda: self.serial_cmd("V%04d" % (float(self.lineEdit.text()) * 100)))
        self.pushButton_6.clicked.connect(lambda: self.serial_cmd("I%04d" % (float(self.lineEdit_2.text()) * 1000)))

    def serial_conn(self):
        if self.ser is None:
            self.ser = Serial('{}'.format(self.comboBox.currentText()),
                              baudrate=int(self.comboBox_2.currentText()),
                              xonxoff=True)
            while True:
                buf = self.ser.read(self.ser.in_waiting)
                QtTest.QTest.qWait(500)
                if buf != b'':
                    break

            self.th_work = Worker(self.ser, parent=self)
            self.th_work.run_state.connect(self.update)
            self.th_work.start()
            self.add_msg('Connected Serial Port')

    def serial_close(self):
        if self.ser is not None:
            self.th_work.running = False
            self.ser.close()
            self.add_msg('Closed Serial Port')
            self.ser = None

    def serial_cmd(self, cmd):
        if self.ser is not None:
            self.ser.write(("{}".format(cmd) + "\r\n").encode('ascii'))
            if cmd == 'N':
                self.add_msg('장비 전원 ON')
            elif cmd == 'F':
                self.add_msg('장비 전원 OFF')
        else:
            self.add_msg('장비 연결이 안되어 있음.')

    def data_stop(self):
        if self.ser is not None:
            self.th_work.running = False

    def data_cont(self):
        self.add_msg('{} | {} | {} | {}'.format(self.label_volt.text(),
                                                self.label_curr.text(),
                                                self.label_pow.text(),
                                                self.label_temp.text()))

    def add_msg(self, text):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('[%Y-%m-%d %H:%M:%S]')
        log_text = str(nowDatetime) + ' ' + text
        self.listWidget.addItem(log_text)
        self.listWidget.scrollToBottom()
        QtTest.QTest.qWait(50)


class Worker(QtCore.QThread):
    run_state = QtCore.pyqtSignal(str)

    def __init__(self, ser, parent=None):
        super(Worker, self).__init__(parent)
        self.parent = parent
        self.ser = ser
        self.running = True

    def run(self):
        while self.running:
            buf = self.ser.read(self.ser.in_waiting)
            QtTest.QTest.qWait(200)
            stat, rest = self.parse_status(buf)
            # print(stat)
            self.parent.label_volt.setText('{} [V]'.format(stat['voltage']))
            QtTest.QTest.qWait(20)
            self.parent.label_curr.setText('{} [A]'.format(stat['current']))
            QtTest.QTest.qWait(20)
            self.parent.label_pow.setText('{} [W]'.format(stat['power']))
            QtTest.QTest.qWait(20)
            self.parent.label_temp.setText('{} [°C]'.format(stat['temperature']))
            QtTest.QTest.qWait(20)
            # print(stat['voltage'])

    def parse_status(self, buf):
        """Extracts first valid log from given buffer. Also returns remaining buffer."""

        #
        # Check match with various possible fragment patterns
        #
        # This is needed as DC6006L emits mixed output of these fragments, instead of
        # emitting single fixed formatted output. So the output is like following:
        #
        #   KB<type0><type1><type3><type0>...<type0><type1><type0><type3><type0>...<type0>
        #
        # First 'KB' prefix is emitted only on first connection setup.
        #
        # On DC580, this prefix seems to be 'MB' and format of each fragment also
        # somewhat differs.
        #
        results = [
            # type-0 fragment
            re.match(''.join([
                '(?P<voltage>\d{4})A', '(?P<current>\d{4})A', '(?P<power>\d{4})A',
                '(\d)A',
                '(?P<temperature>\d{3})A',
                '(?P<mode>\d)A', '(?P<cause>\d)A', '(?P<enable>\d)A',
            ]), buf.decode('ascii')),

            # type-1 fragment
            re.match(''.join([
                '(?P<ovp>\d{4})A', '(?P<ocp>\d{4})A', '(?P<opp>\d{4,5})A',
                '(?P<ohp_enable>\d)A', '(?P<ohp_h>\d\d)A', '(?P<ohp_m>\d\d)A', '(?P<ohp_s>\d\d)A',
            ]), buf.decode('ascii')),

            # type-2 fragment
            re.match(''.join([
                '(?P<target_voltage>\d{4})A', '(?P<target_current>\d{4})A',
            ]), buf.decode('ascii')),

            # type-3 fragment (type-0 with leading garbage)
            re.match(''.join([
                '.*?',
                '(?P<voltage>\d{4})A', '(?P<current>\d{4})A', '(?P<power>\d{4})A',
                '(\d)A',
                '(?P<temperature>\d{3})A',
                '(?P<mode>\d)A', '(?P<cause>\d)A', '(?P<enable>\d)A',
            ]), buf.decode('ascii')),
        ]

        # take the first valid match
        for frag_type, ret in enumerate(results):
            if ret is None: continue

            stat = {}
            for k, v in ret.groupdict().items():
                if v is not None: stat[k] = int(v)

            if frag_type in (0, 3):
                stat['voltage'] /= 100
                stat['current'] /= 1000
                stat['power'] /= 100
                stat['mode'] = 'CV' if stat['mode'] == 0 else 'CC'
                stat['cause'] = ['none', 'OVP', 'OCP', 'OPP', 'OTP', 'OHP'][stat['cause']]

            elif frag_type == 1:
                stat['ovp'] /= 100
                stat['opp'] /= 100

            elif frag_type == 2:
                stat['target_voltage'] /= 100
                stat['target_current'] /= 1000

            return stat, buf[ret.end():]

        return None, buf


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())