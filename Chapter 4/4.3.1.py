# 수치미분 (반올림 오차)
def numerical_diff(f, x):
    h = 10e-50
    return (f(x+h) - f(x)) / h

# 수치미분
def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)  # 중심 차분
