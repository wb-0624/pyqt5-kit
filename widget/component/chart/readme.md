# 注意事项

使用 chart 相关组件时，最好固定大小，而不要跟随父元素大小变化，否则可能会出现window会出现闪烁。
但是如果是原生的 KitWindow 或者 QMainWindow， 就不会出现这个问题。
如果是 KitFramelessWindow 则会出现这个问题。

## 1. 为什么会出现这个问题

暂时还未排查出。使用 pyqtgraph 或者 QtChart 均会出现。

但是两者都是基于 QGraphicsView 的，所以猜测是 QGraphicsView 的问题。

但是自己写的 QGraphicsView 没有出现这个问题。

怀疑是缺少了原生的 WindowTitle 后，部分事件没有处理，导致的问题。