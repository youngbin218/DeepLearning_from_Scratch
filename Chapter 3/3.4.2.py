# 입력층 노드 2개, 1층 노드 3개, 2층 노드 2개, 출력층 노드 2개 구조
import numpy as np

# 1층 노드 A1 및 활성화 함수 적용한 Z1 구현
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape)
print(X.shape)
print(B1.shape)

A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)

print(A1)
print(Z1)

# 2층 노드 A2 구현 및 활성화 함수 적용한 Z2 구현
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

print(A2)
print(Z2)

# 출력층 노드 A3 및 활성화 함수(항등 함수) 적용한 Y 구현
def identity_function(x):
    return x

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

print(Z2.shape)
print(W3.shape)
print(B3.shape)

A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)

print(A3)
print(Y)
