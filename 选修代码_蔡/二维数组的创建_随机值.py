import random
a=[[random.randint(1,5) for i in range(5)] for j in range(5)]
print(a)
for i in range(len(a)):
    print(a[i])