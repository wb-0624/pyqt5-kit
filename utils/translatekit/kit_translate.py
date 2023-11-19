import os
import sys
import xml.dom.minidom as minidom
from feature.excelkit.excel import TableData, write_excel, read_excel
from PyQt5.QtWidgets import QApplication
from config import config

# todo 做个UI界面独立出去做个小工具

_translate = QApplication.translate
# Python环境所在目录
env_path = "D:\\miniconda3\\envs\\ui-platform\\"

# 几个需要用到的工具
# 将py里被标记的字符串提取出来生成ts文件
pylupdate_path = env_path + "Scripts\\pylupdate5.exe"
# 语言家
linguist_path = env_path + "Lib\\site-packages\\qt5_applications\\Qt\\bin\\linguist.exe"
# 将ts文件合并成一个ts文件
lconvert_path = env_path + "Lib\\site-packages\\qt5_applications\\Qt\\bin\\lconvert.exe"
# 将ts文件编译成qm文件
lrelease_path = env_path + "Lib\\site-packages\\qt5_applications\\Qt\\bin\\lrelease.exe"

# 项目根目录
root_path = config.root_path

# 翻译文件保存目录
translate_path = root_path + "language\\"

# 需要生成ts的目录, 会递归遍历,填相对(root_path)的路径即可。
# 不同目录根据倒数第二级的名称来放在不同的文件夹下
dir_list = ["\\system\\ui\\", "\\ui\\ui\\"]
# 排除的目录
exclude_dir = ["__pycache__", ".pytest_cache"]

out_ts_file_name = "app.ts"
out_xlsx_file_name = "app.xlsx"
import_from_xlsx_file_name = "app-new.ts"


def create_ts(dir_path, out_index):
    temp_list = os.listdir(dir_path)
    filename_cmd_list = ""
    ts_name = dir_path.split("\\")[-2]
    output_dir_name = translate_path + out_index + "\\"

    if not os.path.exists(output_dir_name):
        print("创建文件夹:" + output_dir_name)
        os.mkdir(output_dir_name)

    for name in temp_list:
        name_path = dir_path + name
        # 如果是文件
        if os.path.isfile(name_path):
            if not name.endswith(".py") or name.split(".")[0] == "__init__":
                continue
            filename_cmd_list += name_path + " "
        # 目录的处理方式
        if os.path.isdir(name_path):
            if name in exclude_dir:
                continue
            create_ts(name_path + "\\", out_index)

    cmd = pylupdate_path + " " + filename_cmd_list + " -ts " + output_dir_name + ts_name + ".ts"
    os.system(cmd)
    print(dir_path + "下文件已生成完成! -> " + output_dir_name + ts_name + ".ts")


def merge_ts(dir_path):
    """
    合并 目录下的所有ts文件 > out_ts_file_name
    并且删除原来的ts文件
    :return:
    """
    dir_list = os.listdir(dir_path)
    py_list = ""
    for dir_name in dir_list:
        if not os.path.isdir(dir_path + dir_name):
            continue
        for file in os.listdir(dir_path + dir_name):
            py_list += dir_path + dir_name + "\\" + file + " "

    py_list += dir_path + out_ts_file_name + " "

    cmd = lconvert_path + " " + py_list + " -o " + dir_path + "app.ts"
    os.system(cmd)

    print("所有 .ts 文件合并完成! -> " + dir_path + out_ts_file_name)

    # 删除原来的ts文件
    # for file in file_list:
    #     if file == "app.ts":
    #         continue
    #     os.remove(dir_path + file)
    #     print("删除文件: "+dir_path + file)


def open_linguist():
    cmd = linguist_path
    os.system(cmd)


def export_to_excel():
    # 将 ts 文件 转为 xml 文件。
    language_ts = translate_path + out_ts_file_name
    dom = minidom.parse(language_ts)
    root = dom.documentElement
    # 文件头信息
    source_language = root.getAttribute("sourcelanguage")
    target_language = root.getAttribute("language")
    version = root.getAttribute("version")

    headers = ["name/" + version, "source/" + source_language,  "translation/" + target_language]
    keys = ["name", "source", "translation"]
    data = []

    context_list = root.getElementsByTagName("context")
    for context in context_list:
        name = context.childNodes[1].childNodes[0].nodeValue
        message_list = context.getElementsByTagName("message")
        for message in message_list:
            source = message.childNodes[1].childNodes[0].nodeValue
            try:
                translation = message.childNodes[3].childNodes[0].nodeValue
            except Exception as e:
                translation = ""
            data.append({'source': source, "name": name, 'translation': translation})

    table_data = TableData('翻译', headers, keys, data)
    write_excel(translate_path + out_xlsx_file_name, "Sheet", table_data)


def import_from_excel():
    language_xlsx = translate_path + out_xlsx_file_name
    table_data = read_excel(language_xlsx, "Sheet", title_flag=True, keys=["name", "source", "translation"])

    language_xml = translate_path + import_from_xlsx_file_name
    doc_type = minidom.DocumentType("TS")
    dom_impl = minidom.getDOMImplementation()
    dom = dom_impl.createDocument(None, "TS", doc_type)
    root = dom.getElementsByTagName("TS")[0]
    root.setAttribute("version", "2.1")
    root.setAttribute("language", "en")
    root.setAttribute("sourcelanguage", "zh")

    names = []
    for data in table_data.list_data:
        if data.get('name') in names:
            continue
        names.append(data.get('name'))
        name = dom.createElement("name")
        name.appendChild(dom.createTextNode(data.get('name')))
        context = dom.createElement("context")
        context.appendChild(name)
        root.appendChild(context)

    context_list = root.getElementsByTagName("context")

    for data in table_data.list_data:
        index = names.index(data.get('name'))
        context = context_list[index]
        message = dom.createElement("message")

        source = dom.createElement("source")
        source.appendChild(dom.createTextNode(data.get('source')))
        translation = dom.createElement("translation")
        tr = data.get('translation')
        if tr is None or tr == "":
            translation.setAttribute("type", "unfinished")
            tr = ""
        translation.appendChild(dom.createTextNode(tr))
        message.appendChild(source)
        message.appendChild(translation)
        context.appendChild(message)

    with open(language_xml, 'w', encoding='utf-8') as f:
        dom.writexml(f, addindent='\t', newl='\n', encoding='utf-8')


def release_ts_to_qm():
    cmd = lrelease_path + " " + translate_path + out_ts_file_name+ " -qm " + translate_path + "app.qm"
    try:
        os.system(cmd)
    except Exception as e:
        print(e)
    else:
        print("翻译成功! qm文件 -> " + translate_path + "app.qm")


if __name__ == '__main__':

    while True:
        a = input("1. 创建翻译文件ts\n2. 合并ts文件\n3. 打开语言家\n4.ts导出为excel\n5.从excel导入为ts\n6.发布为qm\n7.退出\n")
        if a == "1":
            if not os.path.exists(translate_path):
                print("创建文件夹:" + translate_path)
                os.mkdir(translate_path)
            for i in range(len(dir_list)):
                if not os.path.exists(translate_path + str(i)):
                    os.mkdir(translate_path + str(i))
            for dir_item in dir_list:
                create_ts(root_path + dir_item, str(dir_list.index(dir_item)))
        elif a == "2":
            merge_ts(translate_path)
        elif a == "3":
            open_linguist()
        elif a == "4":
            export_to_excel()
        elif a == "5":
            import_from_excel()
        elif a == "6":
            release_ts_to_qm()
        elif a == "7":
            sys.exit(0)
