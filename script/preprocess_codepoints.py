"""
使用 ttf 文件来显示图标，需要处理一下，将 ttf 文件中的 unicode 转换为对应的字符
通过将 codepoints 文件内容，按照行将 unicode 和 字符分开，存储为字典
这样在使用的时候，就可以通过 icon 名称来设置，而不是 unicode
记得批量替换 \\ -> \
"""


def read_code_points_file(file_url: str, prefix: str = 'i'):
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

        conde_points[prefix + "_" + key] = value

    return conde_points


def write_codepoints_to_class(code_points:dict):
    with open("Icon.py", 'w') as f:
        f.write("class Icons:\n")
        for key in code_points:
            f.write("    {} = \"{}\"\n".format(key, code_points[key]))


if __name__ == "__main__":
    code = read_code_points_file("assets/font/Material-Icons.codepoints", 'md')
    write_codepoints_to_class(code)
