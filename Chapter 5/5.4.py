# 덧셈 게층
class AddLayer:
    def __init__(self):
        pass
        
    def forward(self, x, y):
        out = x + y
        
        return out
    
    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        
        return dx, dy

# 곱셈 계층
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
        
    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        
        return out
    
    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x
        
        return dx, dy
    
# 곱셈 게층 예시 (사과 100원 x 2개 x 세금 10%)
apple = 100
apple_num = 2
tax = 1.1

mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# 순전파
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

print(price)

# 역전파
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print(dapple, dapple_num, dtax)

# 덧셈 & 곱셈 계층 예시 ((사과 100원 x 2개 + 귤 150원 x 3개) x 세금 10%)
apple = 100
apple_num = 2
mandarin = 150
mandarin_num = 3
tax = 1.1

mul_apple_layer = MulLayer()
mul_mandarin_layer = MulLayer()
add_apple_mandarin_layer = AddLayer()
mul_tax_layer = MulLayer()

# 순전파
apple_price = mul_apple_layer.forward(apple, apple_num)
mandarin_price = mul_mandarin_layer.forward(mandarin, mandarin_num)
all_price = add_apple_mandarin_layer.forward(apple_price, mandarin_price)
price = mul_tax_layer.forward(all_price, tax)

print(price)

# 역전파
dprice = 1
dall_price, dtax = mul_tax_layer.backward(dprice)
dapple_price, dmandarin_price = add_layer.backward(dall_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)
dmandarin, dmandarin_num = mul_mandarin_layer.backward(dmandarin_price)

print(dapple, dapple_num, dmandarin, dmandarin_num, dtax)