#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    new_list = list(map(lambda h: replace if h == search else h, my_list))
    return new_list
