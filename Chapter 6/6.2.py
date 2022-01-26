import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

x = np.random.randn(1000, 100)
node_num = 100
hidden_layer_size = 5
activations = {}

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i-1]
    
    # 표준편차 1
    #w = np.random.randn(node_num, node_num) * 1
    # 표준편차 0.01
    #w = np.random.randn(node_num, node_num) * 0.01
    # Xavier 초깃값 (Sigmoid)
    #w = np.random.randn(node_num, node_num) / np.sqrt(node_num)
    # He 초깃값 (ReLU)
    w = np.random.randn(node_num, node_num) * np.sqrt(2 / node_num)
    a = np.dot(x, w)
    #z = sigmoid(a)
    z = relu(a)
    activations[i] = z
    
for i, a in activations.items():
    plt.subplot(1, len(activations), i+1)
    plt.title(str(i+1) + "-layer")
    plt.hist(a.flatten(), 30, range=(0,1))
plt.show()
