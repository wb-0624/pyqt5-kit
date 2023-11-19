# Table组件
## 1. 功能
 - [x] 自定义内部组件
 - [x] 自定义行背景色
 - [x] 自定义交替颜色
 - [x] 自定义列宽，行高
   -  指定 > 自适应 > 100
 - [x] 自定义列对齐方式
 - [x] 冻结效果
 - [x] 分页效果
 - [x] 表头固定效果
 - [x] 表头双击排序，python 内置 sort 通过 Unicode来排序的。
   - [ ] 还需添加排序提示
 - [x] 内容省略，并悬浮提示
 - [x] 多行显示 '_wrap': True
 - [x] 无数据显示

 ## 2. API

### setTableColumnProperty(list)

设置表格列属性

``` python
table.setTableColumnProperty([
    {'key': 'name', 'display': '名称', 'width': 80},
    {'key': 'name2', 'display': '名称2'},
    {'key': 'name3', 'display': '名称3'},
    {'key': 'norad', 'display': '编号', 'width': 300},
    {'key': 'btn', 'display': '操作', 'cell': type(CustomCell()), 'width': 100}
])
```

key：列索引，用于表格显示和数据内容的值对应
display： 表头显示的名称
width: 表格列宽
cell: 自定义单元格，必须继承 TableWidgetCell 类，并且重写 setValue(self, index_data, row_data) 函数。

> 默认情况下表格每列平分整个宽度，不足100的为100。但是通过 width 指定的宽度优先级最高。

### setTableData(list)

设置表格数据

``` python
table.setTableData([
    {'name': '张三', 'name2': '张三2222', 'name3': '张三3333333333333', 'norad': 23942, 'btn': '1'},
    {'name': '李四', 'name2': '李四2', 'name3': '李四3', 'norad': 12902, 'btn': '2'},
    {'name': '王五', 'name2': '王五2', 'name3': '王五3', '_bg': 'lightgreen', 'norad': 12802, 'btn': '3'},
    {'name': '赵六', 'name2': '赵六2', 'name3': '赵六3', 'norad': 12802, 'btn': '12354'},
    {'name': '张三', 'name2': '张三2', 'name3': '张三3', 'norad': 23942, 'btn': '5'},
    {'name': '李四', 'name2': '李四2', 'name3': '李四3', 'norad': 12902, 'btn': '6'},
])
```

json 数据，key 和 setTableColumnProperty 中的 key 对应值，将会放到对应列下。

> 可以使用 '_bg' 来控制行的颜色，优先级高于 斑马纹交替色， 低于 鼠标点击选中颜色。
> 可以使用 '_checked' 来控制改行的 checkbox 是否为勾选。


### setTableCheck(bool)

设置表格第一列是否为 CheckBox。
设置了的话，数据每列索引需要 +1。

``` python
table.setTableCheck(True)
```

### setTableFreezeLeft(int)

设置表格冻结列数量

``` python
table.setTableFreezeLeft(2)
```

### setTablePagination(bool)

是否开启表格分页功能，默认开启。

``` python
table.setTablePagination(True)
```

### setTableCurrentPage(int)

设置当前页码

``` python
table.setTableCurrentPage(1)
```
### setTablePageSum(int)

设置每页的条目数

``` python
table.setTablePageSum(10)
```

### setHeaderRowHeight(int)

设置表格表头高度

``` python
table.setHeaderRowHeight(60)
```

### setBodyRowHeight(int)

设置表格内容行高度
只能设置所有行高度，目前还不持支单独设置某一行。

``` python
table.setBodyRowHeight(60)
```

### getCheckList()

获取选中的行数据

``` python
table.getCheckList()
```