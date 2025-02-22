def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lower = c.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    return chars

def get_sorted_dict(dict):
    list_dict = []
    for char, count in dict.items():
        list_dict.append({char:count})
    def sort_on(dict_item):
        return list(dict_item.values())
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict
