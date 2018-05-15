#!/usr/bin/python3
'problem 1'


class MyList(list):

    'mylist class'

    def print_sorted(self):
        'prints list sorted in ascending order without mutating'
        print(list(sorted(self)))

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/1-my_list.txt")
    
