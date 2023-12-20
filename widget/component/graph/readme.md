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

需要自定义 pyqtgraph 图的画，要继承 KitGraphWidget 类，然后重写 fresh_chart() 方法。

最后发现其实是，窗口的拉伸使用了 ``startSystemResize()` 的原因。应该是 Windows 渲染过快的问题，只需要手动实现拉伸即可。