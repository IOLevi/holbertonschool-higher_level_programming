#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = []
    try:
        for i in range(list_length):
            a.append(my_list_1[i] / my_list_2[i])
    except IndexError:
        print("out of range")
        a.append(0)
    except TypeError:
        print("wrong type")
        a.append(0)
    except ZeroDivisionError:
        print("division by 0")
        a.append(0)
    finally:
        return a
