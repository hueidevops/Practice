# 對串列永久改變順序(sort)，照字母排列順序

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 反向排序
cars.sort(reverse=True)
print(cars)

# 對串列暫時改變順序(sorted)
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list:")
print(cars)

# 反序印出串列reverse()
print(cars)

cars.reverse()
print(cars)

cars.reverse()
print(cars)

# 找出串列長度
print(len(cars))