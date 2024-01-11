from PyQt5.QtCore import Qt

from app_config.constant import Button
import sys


from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from config import config
from widget import KitButton, KitFramelessWindow
from widget.component.table.kit_table import KitTable, TableCellWidget


class CustomCell(TableCellWidget):
    def __init__(self):
        super().__init__()

        self.btn = KitButton()
        self.btn.setType(Button.Primary)
        self.__init_widget()

    def __init_widget(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)

    def setValue(self, index_data, row_data):
        self.btn.setText(str(index_data))


class TableDemo(QWidget):
    def __init__(self, parent=None):
        super(TableDemo, self).__init__(parent=parent)
        layout = QVBoxLayout()
        self.setLayout(layout)
        table = KitTable()
        table.setTableColumnProperty([
            {"display": "序号", "key": "id"},
            {"display": "姓名", "key": "name", 'width': 200, '_wrap': True},
            {"display": "年龄", "key": "age"},
            {"display": "身高", "key": "height", 'cell': type(CustomCell())},
        ])
        table_data = [
            {"id": 1, "name": "张三1289375091 27305781230975091", "age": 18, "height": 180},
            {"id": 2, "name": "李四", "age": 19, "height": {'text': 170}},
            {"id": 3, "name": "王五", "age": 20, "height": {'text': 160}},
            {"id": 4, "name": "赵六", "age": 21, "height": {'text': 150}},
            {"id": 5, "name": "田七", "age": 22, "height": {'text': 140}},
        ]
        table_data_2 = []
        for i in range(100):
            table_data_2.append({"id": i, "name": "张三"+str(i), "age": i, "height": 180})
        table_data_3 = []
        for i in range(80):
            table_data_3.append({"id": i*2, "name": "李四"+str(i), "age": i*2, "height": 170})
        table.setTableShowCheck(True)
        # table.setTablePageSum(2)
        table.setTableLeftFreeze(2)
        table.setBodyRowHeight(60)
        table.setTableData([])
        layout.addWidget(table)
        clear_btn = KitButton('清空')
        clear_btn.clicked.connect(lambda: table.setTableData([]))
        layout.addWidget(clear_btn)

        btn = KitButton('按钮')
        btn.clicked.connect(lambda: table.setTableData(table_data_2))
        layout.addWidget(btn)

        btn2 = KitButton('按钮2')
        btn2.clicked.connect(lambda: table.setTableData(table_data_3))
        layout.addWidget(btn2)

        all = KitButton('全部')
        all.clicked.connect(lambda: print(table.table_data))
        layout.addWidget(all)
        table.freeze_table.table_body.setRowCount(1)



if __name__ == "__main__":

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    config.init()




    window = KitFramelessWindow()
    # window = KitWindow()

    demo = TableDemo()
    window.setCentralWidget(demo)
    window.show()

    sys.exit(app.exec_())
