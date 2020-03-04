#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:28:51 2020

@author: jm385858
"""
import time
  
def zmierz (f, n = 100):
    t0 = time.time()
    f(n)
    t1 = time.time()
    return t1 - t0