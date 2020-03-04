#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:34:05 2020

@author: jm385858
"""

import szybkosc as sz

def silnia(n):
    if n > 1:
        return n * silnia(n - 1)
    else:
        return 1
   
def silnia2(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

def fibonacci(n):
    return 0

print(silnia(100))
print(silnia2(100))

print(sz.zmierz(silnia))
print(sz.zmierz(silnia2))