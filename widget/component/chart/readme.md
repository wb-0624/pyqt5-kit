# 注意事项

使用 chart 相关组件时，最好固定大小，而不要跟随父元素大小变化，否则可能会出现window会出现闪烁。
但是如果是原生的 KitWindow 或者 QMainWindow， 就不会出现这个问题。
如果是 KitFramelessWindow 则会出现这个问题。

## 1. 为什么会出现这个问题

[Borderless Window Flickering while resizing | Qt Forum](https://forum.qt.io/topic/122103/borderless-window-flickering-while-resizing/4)

找到问题原因了，为了实现无边框窗口，对底层的Widget设置了透明。

``` python
self.setAttribute(Qt.WA_TranslucentBackground)
```

是这个设置造成的。

最后在官方找到一个设置可以避免这个问题。但无法确定是否对其他功能有影响。但至少目前对于无边框透明窗口的闪烁效果有极好的效果。

``` python
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
```