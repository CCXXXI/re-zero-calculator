import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

from ui import Ui_MainWindow
from algo import Solver


class UI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.xzq_file = self.para_file = None
        sys.stdout = self
        print('窗口初始化完毕\n')
        self.prt_html('建议先阅读<b><font color="#006000">README.txt</font></b><br>')
        self.prt_html('先指定角色数据文件（如<b><font color="#006000">阿尼茉尼.xlsx</font></b>）和'
                      '心之器数据文件（如<b><font color="#006000">心之器.xlsx</font></b>"），然后导入数据并计算<br>')
        print('若勾选重塑魔法器，会忽略在xlsx文件中填写的魔法器，并按照给定参数自动计算一套最优的魔法器\n')
        print('可以自行指定0到3个心之器，被指定的心之器一定会在结果中出现（这可能导致计算结果不是最优解）\n')
        self.prt_html('有任何bug/问题/建议，可以加群反馈 --> <b><font color="#642100">1011182537</font></b><br>')

    def import_para(self):
        options = QtWidgets.QFileDialog.Options()
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "指定角色数据文件", "", "xlsx文件(*.xlsx)",
                                                            options=options)
        if filename:
            self.para_file = filename
            self.prt_html(f'角色数据文件已指定为<b><font color="#006000">{filename}</font></b><br>')
        self.run_valid()

    def import_xzq(self):
        options = QtWidgets.QFileDialog.Options()
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "指定心之器数据文件", "", "xlsx文件(*.xlsx)",
                                                            options=options)
        if filename:
            self.xzq_file = filename
            self.prt_html(f'心之器数据文件已指定为<b><font color="#006000">{filename}</font></b><br>')
        self.run_valid()

    def run_valid(self):
        valid = self.xzq_file is not None and self.para_file is not None
        self.pushButton_run.setEnabled(valid)

    def set_mfq_enabled(self):
        flag = self.checkBox_mfq.isChecked()
        self.comboBox_mfq.setEnabled(flag)
        self.comboBox_mfq_k.setEnabled(flag)
        self.spinBox_mfq_num.setEnabled(flag)

    def get_mfq_choice(self):
        if not self.checkBox_mfq.isChecked():
            return -1
        else:
            return self.comboBox_mfq.currentIndex()

    def get_xzq_choice(self):
        return {x.text() for x in (self.xzq_1, self.xzq_2, self.xzq_3) if x.text()}

    def write(self, s):
        sys.__stdout__.write(s)
        self.browser.insertPlainText(s)
        # self.browser.moveCursor(self.browser.textCursor().End)
        QtWidgets.QApplication.processEvents()

    def prt_html(self, s):
        sys.__stdout__.write('【html】' + s + '\n')
        self.browser.insertHtml(s + '<br>')
        self.browser.moveCursor(self.browser.textCursor().End)
        QtWidgets.QApplication.processEvents()

    def write_statusbar(self, s):
        sys.__stderr__.write(s)
        self.bar.showMessage(s)

    def flush(self):
        pass

    def run(self):
        self.setEnabled(False)
        ans_para = [2 if self.checkBox_mfq.isChecked() else 3, self.get_xzq_choice()]
        sol = Run(ans_para)
        sol.ans.connect(self.prt_ans)
        sol.write = self.write_statusbar
        sol.load_xzq(self.xzq_file)
        sol.load_role(self.para_file)
        k = [1, 0.975, 0.95, 0.9125, 0.875, 0.8125, 0.75, 0.7, 0.65, 0.575, 0.5][self.comboBox_mfq_k.currentIndex()]
        sol.load_mfq(self.para_file, self.get_mfq_choice(), k, self.spinBox_mfq_num.value())
        sol.start()

    def prt_ans(self, ans):
        self.browser.clear()
        if not ans:
            print('无解')
        for an in ans:
            for a, av in an.items():
                self.prt_html(f'<big><b>{a[1:]}</b></big>')
                temp = []
                if isinstance(av, dict):
                    for key, value in av.items():
                        if isinstance(value, float):
                            value = str(round(value * 100, 2)) + '%'
                        elif isinstance(value, int):
                            value = str(value)
                        temp.append(f'<b>{key}</b>:{value}')
                if isinstance(av, tuple):
                    temp.extend(av)
                if isinstance(av, int):
                    temp.append(str(av))
                self.prt_html('\t'.join(temp))
                print()
            print()
        self.setEnabled(True)


class Run(QThread, Solver):
    ans = pyqtSignal(list)

    def __init__(self, ans_para):
        print('计算线程启动并初始化中……')
        QThread.__init__(self)
        Solver.__init__(self)
        sys.stderr = self
        self.ans_para = ans_para

    def run(self):
        print('计算开始')
        self.ans.emit(self.calc_xzq(*self.ans_para))

    def flush(self):
        pass


if __name__ == "__main__":
    print('【当前环境】window测试v3.0.0')
    app = QtWidgets.QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
