def loss(prediction, target):
    return (target - prediction) ** 2 #محاسبه فاصله دو عدد

print(loss(0.9, 1.0)) # 0.009999999999999995
print(loss(0.5, 1.0)) # 0.25
print(loss(0.1, 1.0))