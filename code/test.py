# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:38:37 2019

@author: s148534
"""

import numpy as np
import matplotlib.pyplot as plt
import registration as reg
import registration_util as util
from registration_tests import image_order_example
from registration_tests import combining_transforms
from IPython.display import display, clear_output

print(reg.identity())

X_rot = reg.rotate(np.pi/4)     #rotation matrix 45 degrees CCW

T_rot=util.t2h(X_rot,np.array([0,0]))
print(T_rot)