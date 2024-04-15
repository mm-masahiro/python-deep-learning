import numpy as np

x = np.array([0, 1]) # input
w = np.array([0.5, 0.5]) # 重み
b = -0.7 # バイアス

w * x
print(np.sum(w * x))
print(np.sum(w * x) + b)



def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7

  tmp = np.sum(w * x) + b
  if tmp <= 0:
    return 0
  return 1

def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = -0.7

  tmp = np.sum(w * x) + b
  if tmp <= 0:
    return 0
  return 1

def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.2

  tmp = np.sum(w * x) + b
  if tmp <= 0:
    return 0
  return 1

def XOR(x1, x2):
  s1 = NAND(x1, x2)
  s2 = OR(x1, x2)
  y = AND(s1, s2)
  return y
  
print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))

print(XOR(0, 0)) # 0を出力
print(XOR(1, 0)) # 1を出力
print(XOR(0, 1)) # 1を出力
print(XOR(1, 1)) # 0を出力
