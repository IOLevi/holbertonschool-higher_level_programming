#!/usr/bin/python3
def roman_to_int(roman_string):
    a = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    b = dict(IV=4, IX=9, XL=40, XC=90, CD=400, CM=900)
    num = 0
    if not isinstance(roman_string, str):
        return 0

    rs = roman_string

    for i in sorted(b.keys()):
        if i in rs:
            num += b[i]
            rs = rs.replace(i, "")

    for i in rs:
        num += a[i]
    return num
