class Theme:
    DARK = "dark"
    LIGHT = "light"


class Button:
    # Button Style
    Text = "text"

    # Button Shape
    Square = "square"
    Round = "round"

    # Button Type
    Primary = "primary"
    Success = "success"
    Warning = "warning"
    Danger = "danger"

    # tool button check state
    UnChecked = "unchecked"
    Checked = "checked"


class Badge:
    Primary = "primary"
    Success = "success"
    Warning = "warning"
    Danger = "danger"
    Info = "info"


class Window:
    resize_margin = 12  # 窗口缩放边界宽度

    Normal = 0
    Minimized = 1
    Maximized = 2
    FullScreen = 3


class ClosePolicy:
    """
    关闭策略
    CloseOnClicked: 点击遮罩层关闭
    CloseOnEscape: 必须调用close函数才能关闭
    """
    CloseOnClicked = 0
    CloseOnEscape = 1


class Position:
    Center = 0
    Left = 1
    Top = 2
    Right = 4
    Bottom = 8
    TopLeft = Top | Left
    TopRight = Top | Right
    BottomLeft = Bottom | Left
    BottomRight = Bottom | Right


class Orientation:
    Horizontal = 0
    Vertical = 1


class Alignment:
    Left = 0
    Top = 1
    Right = 2
    Bottom = 3
    HCenter = 4
    VCenter = 5
    Center = 6


class Graph:
    Histogram = 0
    Line = 1
    Pie = 2
    Scatter = 3
    Polar = 4


class Animation:
    Opacity = 0
    Move = 1
    Geometry = 2


