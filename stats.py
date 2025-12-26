def get_text(filePath):
    with open(filePath) as f:
        text = f.read()
    return text


def get_num_words(text):
    text_l = text.split()
    return len(text_l)


def get_char_num(data):
    char_num = {}
    data = data.lower()
    for d in data:
        if d in char_num:
            char_num[d] += 1
        else:
            char_num[d] = 1

    return char_num


def convert_to_list(dic):
    clist = []
    for d in dic:
        if d.isalpha():
            clist.append({"char": d, "num": dic[d]})

    return clist


def sort_on(items):
    return items["num"]


def list_sort(clist):
    clist.sort(reverse=True, key=sort_on)

    for c in clist:
        print(f"{c['char']}: {c['num']}")
