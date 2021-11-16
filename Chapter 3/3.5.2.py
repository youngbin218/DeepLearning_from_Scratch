import numpy as np

# 오버플로 문제
a = np.array([1010, 1000, 990])
print(np.exp(a) / np.sum(np.exp(a)))

# 문제 개선
c = np.max(a)
print(np.exp(a-c) / np.sum(np.exp(a-c)))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(sum_exp_a)
    y = exp_a / sum_exp_a
    return y
