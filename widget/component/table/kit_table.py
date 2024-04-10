from typing import Dict, List
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QEvent
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QLabel, QTableWidget, QAbstractItemView, QWidget, QVBoxLayout

from ..checkbox import KitCheckBox
from .table_page import TablePagination


class TableCellWidget(QLabel):

    hovered = pyqtSignal()

    def __init__(self, parent=None):
        super(TableCellWidget, self).__init__(parent=parent)
        self.bg_color = None
        self.elide_mode = Qt.ElideRight
        self.wrap_mode = False
        self.index_data = None
        self.row_data = None

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setContentsMargins(4, 0, 4, 0)
        self.setAlignment(Qt.AlignCenter)
        self.setMouseTracking(True)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)

    def initCellValue(self, index_data, row_data):
        self.index_data = index_data
        self.row_data = row_data

        self.setValue(self.index_data, self.row_data)

    def setValue(self, index_data, row_data):
        self.setWordWrap(self.wrap_mode)
        font = self.fontMetrics()
        if font.width(str(self.index_data)) > self.width()-8:
            self.setToolTip(str(self.index_data))
        else:
            self.setToolTip(None)
        if not self.wrap_mode:
            text = font.elidedText(str(self.index_data), self.elide_mode, self.width()-8)
        else:
            text = str(self.index_data)
        self.setText(text)

    def setElideMode(self, elide_mode: Qt.TextElideMode):
        self.elide_mode = elide_mode
        self.update()

    def setBgColor(self, color: str):
        self.bg_color = color
        self.update()

    def sizeHint(self):
        return QSize(100, 40)

    def mousePressEvent(self, ev):
        super().mousePressEvent(ev)

    def mouseMoveEvent(self, ev):
        if self.underMouse():
            self.hovered.emit()

    def paintEvent(self, a0):
        super().paintEvent(a0)
        self.setValue(self.index_data, self.row_data)
        if self.bg_color is not None:
            self.setStyleSheet(self.styleSheet() + f"background-color: {self.bg_color};")


class TableCellCheck(TableCellWidget):

    stateChanged = pyqtSignal(int)

    def __init__(self, tristate=False, parent=None):
        super(TableCellCheck, self).__init__(parent=parent)

        self.check_state = Qt.Unchecked
        self.check = KitCheckBox()
        self.layout = QVBoxLayout()

        self._clicked = False

        if tristate:
            self.check.setTristate(True)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def setValue(self, index_data, row_data):
        if index_data is None:
            return
        self.setCheckState(index_data)

    def __init_widget(self):
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.layout.addWidget(self.check, alignment=Qt.AlignHCenter)
        self.check.installEventFilter(self)

    def __init_slot(self):
        self.check.stateChanged.connect(lambda: self.setCheckState(self.check.checkState()))
        self.stateChanged.connect(lambda i: self.check.setCheckState(i))

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setCheckState(self, state: Qt.CheckState):
        if self.check_state == state:
            return
        if self._clicked and self.check.checkState() == Qt.PartiallyChecked:
            self.check_state = Qt.Checked
        else:
            self.check_state = state
        self._clicked = False
        self.stateChanged.emit(self.check_state)
        self.update()

    def checkState(self):
        return self.check_state

    def eventFilter(self, a0, a1) -> bool:
        if (a1.type() == QEvent.MouseButtonPress or a1.type() == QEvent.MouseButtonDblClick) and self.check.isTristate():
            self._clicked = True
        return super().eventFilter(a0, a1)


class TableBase(QTableWidget):

    tableColumnPropertyChanged = pyqtSignal(list)
    tableDataChanged = pyqtSignal(list)
    tableShowChecked = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(TableBase, self).__init__(parent=parent)

        self.table_column_property = []
        self.row_height = 40
        self.check_cell_width = 40
        self.column_hint_width = 100
        self.table_data: List[Dict] = []
        self.show_check = False

        self.if_fit_width = True

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setShowGrid(False)
        self.setAutoScroll(False)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setTableColumnProperty(self, table_column_property: list):
        if self.table_column_property != table_column_property:
            self.table_column_property = table_column_property
        self.tableColumnPropertyChanged.emit(table_column_property)

    def setTableData(self, table_data: list):
        if self.table_data != table_data:
            self.table_data = table_data
        self.tableDataChanged.emit(table_data)

    def setShowCheck(self, show: bool):
        if self.show_check != show:
            self.show_check = show
        self.tableShowChecked.emit(show)

    def setRowChecked(self, row):
        if self.show_check and 0 <= row < len(self.table_data) and isinstance(self.table_data[row], dict):
            self.cellWidget(row, 0).setCheckState(Qt.Checked)
            self.table_data[row]['_checked'] = True

    def setRowUnChecked(self, row):
        if self.show_check and 0 <= row < len(self.table_data) and isinstance(self.table_data[row], dict):
            self.cellWidget(row, 0).setCheckState(Qt.Unchecked)
            self.table_data[row]['_checked'] = False

    def checkAll(self):
        if self.show_check:
            for row in range(self.rowCount()):
                self.setRowChecked(row)

    def uncheckAll(self):
        if self.show_check:
            for row in range(self.rowCount()):
                self.setRowUnChecked(row)

    def __fresh_column_width(self):
        share_width_column = len(self.table_column_property)
        view_width = self.viewport().width()
        column_width = [0] * share_width_column
        if self.show_check:
            view_width -= self.check_cell_width

        for column in range(len(self.table_column_property)):
            if self.table_column_property[column].get('width') is not None:
                column_width[column] = int(self.table_column_property[column].get('width'))
                view_width -= column_width[column]
                share_width_column -= 1

        for column in range(len(self.table_column_property)):
            if column_width[column] == 0:
                column_width[column] = view_width // share_width_column \
                    if view_width // share_width_column > self.column_hint_width else self.column_hint_width

        if self.show_check:
            column_width.insert(0, 40)

        for column in range(self.columnCount()):
            self.setColumnWidth(column, column_width[column])

    def __fresh_row_height(self):
        for row in range(self.rowCount()):
            self.setRowHeight(row, self.row_height)

    def __fresh_cell_size(self):
        # 调整单元格大小 TableCellWidget
        for column in range(self.columnCount()):
            for row in range(self.rowCount()):
                item = self.cellWidget(row, column)
                if isinstance(item, TableCellWidget):
                    item.setFixedSize(self.columnWidth(column), self.rowHeight(row))

    def resizeEvent(self, e) -> None:
        super().resizeEvent(e)
        if self.if_fit_width:
            self.__fresh_column_width()
        self.__fresh_row_height()
        self.__fresh_cell_size()


class TableHeader(TableBase):

    headerCheckChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(TableHeader, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.verticalScrollBar().setVisible(False)

    def __init_slot(self):
        self.tableDataChanged.connect(self.__fresh_table_header)
        self.tableColumnPropertyChanged.connect(self.__fresh_table_header)
        self.tableShowChecked.connect(self.__fresh_table_header)

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setHeaderRowHeight(self, height: int):
        self.row_height = height
        self.__fresh_table_header()

    def setHeaderCheckState(self, state):
        if self.show_check:
            widget = self.cellWidget(0, 0)
            if type(widget) == TableCellCheck:
                widget.setCheckState(state)

    def __fresh_table_header(self):
        self.setRowCount(1)
        self.setFixedHeight(self.row_height)
        offset = 1 if self.show_check else 0
        self.setColumnCount(len(self.table_column_property) + offset)
        for column in range(self.columnCount()):
            property_column = column - offset
            if property_column == -1:
                table_cell_widget = TableCellCheck(True, self)
                table_cell_widget.stateChanged.connect(self.headerCheckChanged.emit)
            else:
                table_cell_widget = TableCellWidget(self)
                table_cell_widget.initCellValue(self.table_column_property[property_column]["display"], self.table_column_property[property_column])
            self.setCellWidget(0, column, table_cell_widget)

        self.resizeEvent(QResizeEvent(self.size(), self.size()))


class TableBody(TableBase):

    rowCheckedChanged = pyqtSignal(int, bool)
    rowHovered = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super(TableBody, self).__init__(parent=parent)

        self.current_row = -1
        self.hovered_row = -1
        self.alternate_row_color = True

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def __init_slot(self):
        self.tableColumnPropertyChanged.connect(self.__fresh_table_body)
        self.tableDataChanged.connect(self.__fresh_table_body)
        self.tableShowChecked.connect(self.__fresh_table_body)

        self.currentCellChanged.connect(lambda current_row, current_column, previous_row, previous_column:
                                        self.__handle_current_row_changed(current_row, previous_row))

        self.rowHovered.connect(lambda row, previous_row: self.__handle_row_hovered(row, previous_row))

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setTableAlternateRowColor(self, alternate: bool):
        self.alternate_row_color = alternate
        self.__fresh_table_body()

    def setBodyRowHeight(self, height: int):
        self.row_height = height
        self.__fresh_table_body()

    def __fresh_table_body(self):
        if self.table_data is None or len(self.table_data) == 0:
            self.clear()
            self.setRowCount(2)
            column = len(self.table_column_property)
            if self.show_check:
                column += 1
            self.setColumnCount(column)
            cell = QLabel()
            cell.setObjectName('table_none')
            cell.resize(self.viewport().width(), self.row_height * 2)
            cell.setStyleSheet('background-color:rgba(100,100,100,20)')
            cell.setText('暂无数据')
            cell.setAlignment(Qt.AlignCenter)
            self.setCellWidget(0, 0, cell)
            self.setSpan(0, 0, 3, column+1)
            return

        self.clearSpans()
        offset = 1 if self.show_check else 0
        self.setColumnCount(len(self.table_column_property) + offset)
        self.setRowCount(len(self.table_data))

        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                property_column = column - offset
                if property_column == -1:
                    table_cell_widget = TableCellCheck()
                    if self.table_data[row].get('_checked'):
                        table_cell_widget.setCheckState(Qt.Checked)
                    else:
                        table_cell_widget.setCheckState(Qt.Unchecked)
                    table_cell_widget.stateChanged.connect(lambda state, r=row: self.__handle_row_checked(r, state))
                else:
                    if self.table_column_property[property_column].get("cell") is None:
                        table_cell_widget = TableCellWidget()
                        table_cell_widget.hovered.connect(lambda r=row: self.rowHovered.emit(r, self.hovered_row))
                    else:
                        table_cell_widget = self.table_column_property[property_column].get('cell')()

                    if self.table_column_property[property_column].get("_wrap"):
                        table_cell_widget.wrap_mode = True
                    table_cell_widget.initCellValue(self.table_data[row].get(self.table_column_property[property_column]["key"]), self.table_data[row])

                self.__init_cell_color(row, table_cell_widget)
                self.setCellWidget(row, column, table_cell_widget)
        self.resizeEvent(QResizeEvent(self.size(), self.size()))
        self.setCurrentCell(self.current_row, self.currentColumn())

    def __init_cell_color(self, row, widget):
        if (row < 0 or row >= self.rowCount()
            or widget is None
            or self.table_data is None
            or len(self.table_data) == 0
        ):
            return

        widget.setStyleSheet('')

        # 当前行被选中的颜色
        if row == self.current_row:
            widget.setProperty('row', 'current')
            widget.style().polish(widget)
            return widget

        # 当前行被悬浮的颜色
        if row == self.hovered_row:
            widget.setProperty('row', 'hovered')
            widget.style().polish(widget)
            return widget

        # 表格指定行变色
        if self.table_data[row].get('_bg') is not None and self.table_data[row].get('_bg') != '':
            widget.setStyleSheet(
                self.styleSheet() + f'TableCellWidget{{background-color:{self.table_data[row].get("_bg")}}};')
            return widget

        # 表格交替行变色
        if self.alternate_row_color:
            if row % 2 == 0:
                widget.setProperty('row', 'even')
            else:
                widget.setProperty('row', 'odd')
        else:
            widget.setProperty('row', None)

        widget.style().polish(widget)
        return widget

    def __handle_current_row_changed(self, current_row, previous_row):
        self.current_row = current_row
        for column in range(self.columnCount()):
            widget = self.cellWidget(self.current_row, column)
            self.__init_cell_color(self.current_row, widget)
            previous_widget = self.cellWidget(previous_row, column)
            self.__init_cell_color(previous_row, previous_widget)

    def __handle_row_checked(self, row, check):
        if check == Qt.Checked:
            self.setRowChecked(row)
        if check == Qt.Unchecked:
            self.setRowUnChecked(row)
        self.rowCheckedChanged.emit(row, check)

    def setHoverRow(self, row):
        self.__handle_row_hovered(row, self.hovered_row)

    def __handle_row_hovered(self, current_row, previous_row):
        if current_row == previous_row:
            return
        self.hovered_row = current_row
        for column in range(self.columnCount()):
            widget = self.cellWidget(current_row, column)
            self.__init_cell_color(current_row, widget)
            previous_widget = self.cellWidget(previous_row, column)
            self.__init_cell_color(previous_row, previous_widget)


class TableMain(TableBase):

    def __init__(self, parent=None):
        super(TableMain, self).__init__(parent=parent)

        self.table_header = TableHeader()
        self.table_body = TableBody()

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.layout.addWidget(self.table_header)
        self.layout.addWidget(self.table_body)

    def __init_slot(self):
        self.table_body.horizontalScrollBar().valueChanged.connect(self.table_header.horizontalScrollBar().setValue)

        self.table_header.headerCheckChanged.connect(self.__handle_header_check)
        self.table_body.rowCheckedChanged.connect(self.__handle_body_check)

        self.table_header.cellDoubleClicked.connect(lambda row, column: self.sortByColumnUnicode(column))

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setTableData(self, table_data: list):
        super().setTableData(table_data)
        self.table_body.setTableData(table_data)
        self.table_header.setTableData(table_data)
        self.__handle_body_check()

    def setTableColumnProperty(self, table_column_property: list):
        super().setTableColumnProperty(table_column_property)
        self.table_body.setTableColumnProperty(table_column_property)
        self.table_header.setTableColumnProperty(table_column_property)

    def sortByColumnUnicode(self, column):
        if self.show_check:
            column -= 1
        order = 'up' if self.table_column_property[column].get('_sort') == 'down' else 'down'
        self.table_column_property[column]['_sort'] = order
        if self.table_data is not None and len(self.table_data) > 0:
            index_data = self.table_data[0].get(self.table_column_property[column]['key'])
            if isinstance(index_data, dict):
                return self.table_data
        self.table_data.sort(key=lambda x: x[self.table_column_property[column]['key']], reverse=order == 'down')
        self.setTableData(self.table_data)
        return self.table_data

    def setShowCheck(self, show: bool):
        super().setShowCheck(show)
        self.table_body.setShowCheck(show)
        self.table_header.setShowCheck(show)

    def __handle_header_check(self, state):
        if state == Qt.Checked:
            self.table_body.checkAll()
            self.table_header.setHeaderCheckState(Qt.Checked)
        elif state == Qt.Unchecked:
            self.table_body.uncheckAll()
            self.table_header.setHeaderCheckState(Qt.Unchecked)

    def __handle_body_check(self):
        state = 0
        for item in self.table_data:
            if item.get('_checked'):
                state += 1
        if state == len(self.table_data) and len(self.table_data) > 0:
            self.table_header.setHeaderCheckState(Qt.Checked)
        elif state > 0:
            self.table_header.setHeaderCheckState(Qt.PartiallyChecked)
        else:
            self.table_header.setHeaderCheckState(Qt.Unchecked)

    def getCurrentRow(self):
        return self.table_body.current_row

    def getCurrentRowData(self):
        return self.table_data[self.get_current_row()]

    def setHeaderRowHeight(self, height):
        self.table_header.setHeaderRowHeight(height)

    def setBodyRowHeight(self, height):
        self.table_body.setBodyRowHeight(height)

    def setColumnWidth(self, column: int, width: int) -> None:
        self.table_body.setColumnWidth(column, width)
        self.table_header.setColumnWidth(column, width)
        self.table_header.resizeEvent(QResizeEvent(
            QSize(self.table_body.columnWidth(column), self.table_header.height()),
            QSize(self.table_body.columnWidth(column), self.table_header.height())
        ))
        self.table_body.resizeEvent(QResizeEvent(
            QSize(self.table_body.columnWidth(column), self.table_body.height()),
            QSize(self.table_body.columnWidth(column), self.table_body.height())
        ))

    def columnWidth(self, column: int) -> int:
        return self.table_body.columnWidth(column)

    def resizeEvent(self, e) -> None:
        super().resizeEvent(e)
        self.table_header.resizeEvent(e)
        self.table_body.resizeEvent(e)


class TableFreeze(TableMain):

    def __init__(self, parent=None):
        super(TableFreeze, self).__init__(parent=parent)

        self.freeze_column_left = 0

        self.table_freeze = TableMain(self)
        self.table_freeze.setObjectName('table_freeze')

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        # 冻结部分
        self.table_freeze.table_body.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_freeze.table_body.verticalScrollBar().setVisible(False)
        self.table_freeze.table_body.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_freeze.table_body.horizontalScrollBar().setVisible(False)
        self.table_freeze.table_header.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_freeze.table_header.verticalScrollBar().setVisible(False)

        self.table_freeze.table_header.if_fit_width = False
        self.table_freeze.table_body.if_fit_width = False
        # 非冻结部分
        self.table_body.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def __init_slot(self):
        # 垂直方向同步滚动
        self.table_body.verticalScrollBar().valueChanged.connect(self.table_freeze.table_body.verticalScrollBar().setValue)
        self.table_freeze.table_body.verticalScrollBar().valueChanged.connect(self.table_body.verticalScrollBar().setValue)

        # 当前单元格同步
        self.table_body.currentCellChanged.connect(self.table_freeze.table_body.setCurrentCell)
        self.table_freeze.table_body.currentCellChanged.connect(self.table_body.setCurrentCell)

        # 同步排序
        self.table_freeze.table_header.cellDoubleClicked.connect(lambda: self.setTableData(self.table_freeze.table_data))

        # 悬浮同步
        self.table_body.rowHovered.connect(self.table_freeze.table_body.setHoverRow)
        self.table_freeze.table_body.rowHovered.connect(self.table_body.setHoverRow)

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setLeftFreeze(self, freeze_column_left: int):
        self.freeze_column_left = freeze_column_left
        if self.freeze_column_left > 0:
            self.table_body.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        else:
            self.table_body.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.__fresh_freeze_table_size()

    def setTableColumnProperty(self, table_column_property: list):
        super().setTableColumnProperty(table_column_property)
        self.table_freeze.setTableColumnProperty(table_column_property)

    def setTableData(self, table_data: list):
        super().setTableData(table_data)
        self.table_freeze.setTableData(table_data)
        self.table_freeze.setVisible(True)
        if self.table_data is None or len(self.table_data) == 0:
            self.table_freeze.setVisible(False)
        self.__fresh_freeze_table_size()

    def setShowCheck(self, show: bool):
        super().setShowCheck(show)
        self.table_freeze.setShowCheck(show)

    def setHeaderRowHeight(self, height):
        super().setHeaderRowHeight(height)
        self.table_freeze.setHeaderRowHeight(height)

    def setBodyRowHeight(self, height):
        super().setBodyRowHeight(height)
        self.table_freeze.setBodyRowHeight(height)

    def __fresh_freeze_table_size(self):
        self.table_body.update()
        width = 0
        for column in range(self.freeze_column_left):
            width += self.table_body.columnWidth(column)
        self.table_freeze.resize(width, self.height()-self.table_body.horizontalScrollBar().height())
        for column in range(self.table_freeze.columnCount()):
            self.table_freeze.setColumnHidden(column, True)
        for left in range(self.freeze_column_left):
            self.table_freeze.setColumnHidden(left, False)
            self.table_freeze.setColumnWidth(left, self.table_body.columnWidth(left))

    def resizeEvent(self, e) -> None:
        super().resizeEvent(e)
        self.__fresh_freeze_table_size()


class KitTable(QWidget):

    def __init__(self, parent=None):
        super(KitTable, self).__init__(parent=parent)

        self.table_data = []
        self.table_current_page_data = []
        self.table_column_property = []
        self.freeze_table = TableFreeze()
        self.show_pagination = True
        self.page = TablePagination()

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.layout.addWidget(self.freeze_table, 1)
        self.layout.addWidget(self.page)

        self.setTableData([])

    def __init_slot(self):
        self.page.currentPageChanged.connect(lambda page, page_data: self.__fresh_current_page_data(page_data))

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def resizeEvent(self, a0) -> None:
        super().resizeEvent(a0)
        self.freeze_table.resizeEvent(a0)

    def setTableColumnProperty(self, table_column_property):
        self.table_column_property = table_column_property
        self.freeze_table.setTableColumnProperty(table_column_property)

    def setTableData(self, table_data: list):
        self.table_data = table_data
        self.freeze_table.setTableData(table_data)
        self.__fresh_page_table_data()

    def __fresh_page_table_data(self):
        if self.show_pagination:
            self.page.setAllData(self.table_data)

    def __fresh_current_page_data(self, data: list):
        self.table_current_page_data = data
        self.freeze_table.setTableData(data)

    def setTableShowCheck(self, check: bool):
        self.freeze_table.setShowCheck(check)

    def setTableLeftFreeze(self, freeze_column_left: int):
        self.freeze_table.setLeftFreeze(freeze_column_left)

    def setTablePagination(self, show: bool):
        self.show_pagination = show
        self.page.setVisible(show)
        self.setTableData(self.table_data)

    def setTableCurrentPage(self, page):
        self.page.setCurrentPage(page)

    def setTablePageSum(self, page_sum):
        self.page.setPageSum(page_sum)

    def getCheckList(self):
        return [row_data for row_data in self.freeze_table.table_data if row_data.get('_checked')]

    def setHeaderRowHeight(self, height):
        self.freeze_table.setHeaderRowHeight(height)

    def setBodyRowHeight(self, height):
        self.freeze_table.setBodyRowHeight(height)
