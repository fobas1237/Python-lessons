my_list = [8, None, 'a', True, 9.5]


def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


my_type(my_list)
