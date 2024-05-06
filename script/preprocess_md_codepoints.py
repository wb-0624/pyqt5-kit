"""
使用 ttf 文件来显示图标，需要处理一下，将 ttf 文件中的 unicode 转换为对应的字符
通过将 codepoints 文件内容，按照行将 unicode 和 字符分开，存储为一个类。
这样在使用的时候，就可以通过 icon 名称来设置，而不是 unicode
"""


def read_code_points_file(file_url: str, prefix: str = "i"):
    conde_points = {}
    with open(file_url, "r") as f:
        # 读取文件每一行
        lines = f.readlines()
        # 去除每一行的换行符
        lines = [line.strip() for line in lines]

    for line in lines:
        line_list = line.split(" ")
        key = line_list[0]
        value = line_list[1]
        # 给所有的 key 添加前缀,是为了避免某些开头为数字,或者key是保留字的情况
        conde_points[prefix + "_" + key] = value

    return conde_points


def write_codepoints_to_class(code_points: dict, prefix: str, class_file_url: str):
    with open(class_file_url + prefix + "_icons.py", "w") as f:
        f.write("class " + prefix[0].upper() + prefix[1:] + "Icons:\n")
        for key in code_points:
            f.write('    {} = "\\u{}"\n'.format(key, code_points[key]))


def generate_icon_class(icon_font_url: str, prefix: str, class_file_url: str):
    """
    生成 icon class
    :param icon_font_url: codepoints 文件路径
    :param prefix: icon 前缀。如 md, 生成的class为 MdIcons。使用为 MdIcons.md_XXX
    :param class_file_url: 生成的 class 文件路径，以 / 结尾。
    """
    code = read_code_points_file(icon_font_url, prefix)
    write_codepoints_to_class(code, prefix, class_file_url)


if __name__ == "__main__":
    generate_icon_class("assets/font/Material-Icons.codepoints", "md", "app_config/")
