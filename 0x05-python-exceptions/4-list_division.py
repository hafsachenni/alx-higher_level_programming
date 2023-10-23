#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            list1 = my_list_1[i] if  i < len(my_list_1) else 1
            list2 = my_list_2[i] if i < len(my_list_2) and my_list_2[i] != 0 else 1
            result = list1 / list2
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
