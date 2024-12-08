
def parsed(enter_names):
    new_list = enter_names.split(",")
    return new_list


def detect_len(name_list):
    return len(name_list)


enter_name = input("Enter names separated bt commas (no space): ")

list_parsed = parsed(enter_name)
print(detect_len(list_parsed))