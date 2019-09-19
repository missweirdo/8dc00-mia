# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:38:37 2019

@author: s148534
"""
# %%
import numpy as np
import matplotlib.pyplot as plt
import registration as reg
import registration_util as util
from registration_tests import image_order_example
from registration_tests import combining_transforms
from IPython.display import display, clear_output

x = np.arange(0, 5)
y = np.arange(0, 6)
xx, yy = np.meshgrid(x, y,sparse=True)

print(xx)
print(yy)
