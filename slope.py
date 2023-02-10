# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 19:02:21 2023

@author: lilbl
"""
def slope(xs,ys,newx):
    m=(ys(1)-ys(0))/(xs(1)-xs(0))
    b=ys(1)-m*xs(1)
    newy=m*newx+b
    return newy
