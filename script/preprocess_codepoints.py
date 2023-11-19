"""
使用 ttf 文件来显示图标，需要处理一下，将 ttf 文件中的 unicode 转换为对应的字符
通过将 codepoints 文件内容，按照行将 unicode 和 字符分开，存储为字典
这样在使用的时候，就可以通过 icon 名称来设置，而不是 unicode
记得批量替换 \\ -> \
"""

# 下面的 icon 名称会和 python 内置的关键字冲突，需要排除
# 排除数组开头的
exclude_list = [
    "class", "try", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]


def read_conde_points_file(file_url:str):
    lines = []
    conde_points = {}
    with open(file_url, 'r') as f:
        # 读取文件每一行
        lines = f.readlines()
        # 去除每一行的换行符
        lines = [line.strip() for line in lines]

    for line in lines:
        line_list = line.split(" ")
        key = line_list[0]
        value = "\\u" + line_list[1]
        if key not in exclude_list and key[0] not in exclude_list:
            conde_points[key] = value

    print(conde_points)



if __name__ == "__main__":
    read_conde_points_file("assets/font/Material-Icons.codepoints")
