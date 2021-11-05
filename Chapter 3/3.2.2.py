# 단순 구현
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0
    
# numpy 지원 구현
def step_function(x):
    y = x > 0
    return y.astype(np.int64)
