# 主题

样式上，采用了scss，为了可以使用变量，方便主题的切换。

在 theme/common 下，是一些通用的样式变量，主要用到的还是颜色。

在 theme/component 下， 则是对组件样式的详细设置。

当然一般情况下，可以不必理会这两个文件下的内容。

关注一下 light.scss。这里对组件详细部分的样式定义了变量，这些变量也在 component 下的对应组件的 scss 文件中使用。

所以只需要在theme下，创建其他的主题文件，然后实现所有的变量即可。

# 如何自定义主题

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