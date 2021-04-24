# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:27:00 2021

@author: carols1107
"""

import  HumanClass
David = HumanClass.Human(' David',100,100)
print(David.name, 'bmi' ,David.bmi())

Jenny = HumanClass.Woman('Jenny',40,100,40,20,10)
print(Jenny.name, 'bmi' ,Jenny.bmi())
Jenny.printBWH()

    