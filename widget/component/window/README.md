# 窗口

无论是有边框还是无边框，都添加了发射 windowSizeChanged 信号。用来更新一些依赖于窗口大小的组件。

- frameless_window.py  无边框窗口
- window_body.py       窗口主体
- title_bar.py         标题栏
- status_bar.py        状态栏
- kit_window.py        有边框窗口

这里的titlebar实现了窗口移动。如果设置titlebar为None的话，会失去移动效果，需要自己实现。
这里建立删除titlebar里的东西，而不是直接删除titlebar。

``` python

基础仍然是QMainWindow。

``` python
self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
self.setAttribute(Qt.WA_TranslucentBackground)

self.window_body = WindowBody()
self.title_bar = self.window_body.title_bar

self.setCentralWidget(self.window_body)
self.resize(800, 600)
```

只不过把 QMainWindow 内部的 centralWidget 部分作为新的窗口。

title_bar通过 init 时的 parent 和WindowBody建立联系。

并且通过qss对WindowBody设置阴影等。

# ToDo
- [x] 最大化，最小化，关闭，还原，全屏。
- [x] 双击标题栏，最大化，还原。
- [x] 按住标题栏移动。
- [x] 边框拉伸。
- [x] 贴靠顶部最大化，拉开还原。 

# 问题
- [ ] 无边框窗口的边框阴影会导致内部其他组件使用透明度变化动画时，发生位置偏移。和阴影的 blurRadius 有关。