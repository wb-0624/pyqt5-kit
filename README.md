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


# component

关于 KitPopup, KitLoading, KitModal, KitMessage, KitOverlay 的使用说明：
由于它们不需要指定父控件，而是根据 QApplication.activeWindow() 来创建的。所以在使用这些组件前必须确保当前窗口是被激活的。
如果无法控制用户的操作，需要在执行相关组件前，先调用以下函数来激活窗口。

``` python 
QApplication.setActiveWindow(self)
```

这里的self必须是在当前窗口中的一个控件，否则无法激活窗口。

只有在外部条件触发时，需要额外注意。如果是通过按钮等触发，则不需要考虑该问题。


# Theme

- 通常情况下只需要在 `theme` 下建立主体文件，例如: `light.scss` 。并且参照其内的样式变量实现自定义的样式。
``` css
$color-primary: #3f51b5;
```

- 如果需要添加额外的预定义变量， 在 `common` 下创建  `.scss` 文件即可。

``` css
$white: white;
```

- 如果需要添加额外的组件修改变量， 修改component下的对应的组件的scss文件即可。例如需要为button组件贴图。

``` css
KitButton{
    border-image: $button-border-image;
}
```

> 切勿在 `component` 下的文件内使用 import 语句。
> 要记得在主题变量文件中添加该变量并赋值。