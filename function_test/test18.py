import os

path_var = "/Users/baojie/Documents/python/learn/python_learn"


def get_all_size(path_var):
    size = 0
    lst = os.listdir(path_var)
    print(lst)
    for i in lst:
        path_var2 = os.path.join(path_var, i)
        if os.path.isdir(path_var2):
            size += get_all_size(path_var2)
        elif os.path.isfile(path_var2):
            size += os.path.getsize(path_var2)

    return size


res = get_all_size(path_var)
print(res)
