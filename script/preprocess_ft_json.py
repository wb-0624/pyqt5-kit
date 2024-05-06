import json


def read_fluent_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


def write_icon_class(data, class_file_url, file_name, class_name, prefix):
    with open(class_file_url + file_name + ".py", "w", encoding="utf-8") as f:
        f.write("class " + class_name + ":\n")
        for key, value in data.items():
            correct_unicode = chr(value).replace("\\\\", "\\")
            string = correct_unicode.encode("unicode-escape").decode("utf-8")
            f.write("    " + prefix + '_{} = "{}"\n'.format(key, string))


if __name__ == "__main__":
    data_map = {}

    # regular icon
    regular_data = read_fluent_json("assets/font/FluentSystemIcons-Regular.json")
    for key, value in regular_data.items():
        # ic_fluent_clock_24_regular -> clock
        if "24" in key:
            key = key.replace("ic_fluent_", "")
            key = key.replace("24_", "")
            key = key.replace("_regular", "")
            data_map[key] = value
    # fill icon
    fill_data = read_fluent_json("assets/font/FluentSystemIcons-Filled.json")
    for key, value in fill_data.items():
        # ic_fluent_clock_24_filled -> clock_filled
        if "24" in key:
            key = key.replace("ic_fluent_", "")
            key = key.replace("24_", "")
            data_map[key] = value

    write_icon_class(data_map, "app_config/", "ft_icons", "FluentIcons", "ft")
