# 无边框窗口

- frameless_window.py  无边框窗口
- window_body.py       窗口主体
- title_bar.py         标题栏
- status_bar.py        状态栏

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
- [ ] 贴靠顶部最大化，拉开还原。 