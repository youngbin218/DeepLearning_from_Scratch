# 0 (b + x1*w1 + x2*w2 <= 0)
# 1 (b + x1*w1 + x2*w2 > 0)

import numpy as np
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7

np.sum(w*x) + b
