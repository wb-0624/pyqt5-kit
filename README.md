# 启动

运行前，要把运行目录改为工程根目录。

# theme

在样式上，采用了 sass 。

可以预定义一系列的变量用于样式的定义。

即使写qss，也是以文本的方式赋值过去。 将其编译之后的样式代码，以文本方式赋予了应用即可。

但是要注意，有些pyqt独有的样式写法，如果写在scss里，编译就会出错，只能拆分一个独立的qss来写。

# Icon

https://developers.google.com/fonts/docs/material_icons

``` python
Icons.close
```


# script

自己写的一些脚本，用于快速生成一些文件。
