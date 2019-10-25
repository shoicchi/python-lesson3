def find_index(the_list, target):
    idx = 0
    for item in the_list:
        if target == item:
            return idx
    idx = idx + 1

