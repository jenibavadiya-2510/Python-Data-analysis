
# Mathematical operations

import numpy as np

# a = np.array([10, 20, 30, 40, 50])
# print(np.sum(a))
# print(np.mean(a))
# print(np.median(a))
# print(np.std(a))
# print(np.var(a))
# print(np.min(a))
# print(np.max(a))
# print(np.argmin(a))
# print(np.argmax(a))
# print(np.prod(a))
# print(np.cumsum(a))
# print(np.cumprod(a))


# Reshapping array

# a = np.array([[10,20,30],[40,50,60]])
# print(a.reshape(3,2))
# print(a.flatten())
# print(a.ravel())
# print(a.transpose())
# print(np.resize(a,(3,4)))


# array operations

# a = np.array([10, 20, 30])
# b = np.array([2, 4, 5])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a ** b)
# print(np.sqrt(a))
# print(np.abs(a))
# print(np.exp(a))

# c = np.array([10.456, 20.789, 30.123])
# print(np.round(c))
# print(np.round(c, 2))

# filtering & conditions
# a = np.array([10, 20, 30, 40, 50])
# b = np.array([10, np.nan, 30, np.inf, 50])
# print(a[a>25])
# print(a>25)
# print(a==30)
# print(a[(a>20) & (a<50)])
# print(a[(a<20) | (a==50)])
# print(np.where(a>25, "pass", "fail"))
# print(np.any(a>45))
# print(np.all(a>5))
# print(np.isnan(b))
# print(np.isfinite(b))

# Random module
# np.random.seed(20)
# print(np.random.rand(3))
# print(np.random.randint(1, 10, 5))
# print(np.random.random(4))
# print(np.random.choice([10, 20, 30, 40, 50], 3))

# a = np.array([10, 20, 30, 40, 50])
# np.random.shuffle(a)
# print(a)

# b = np.array([1, 2, 3, 4, 5])
# print(np.random.permutation(b))
# print(b)








