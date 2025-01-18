def generate_xml_by_list(open_tag: str, value_list: list, close_tag: str) -> str:
    result = ""

    for i in range(len(value_list)):
        if i != len(value_list) - 1:
            result += open_tag + str(value_list[i]) + close_tag + "\n"
        else:
            result += open_tag + str(value_list[i]) + close_tag
    return result

