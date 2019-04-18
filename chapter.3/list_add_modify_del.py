# 修改串列中的元素
motorcycle = ["honda", "yamaha", "suzuki"]
print(motorcycle)

motorcycle[0] = 'ducati'
print(motorcycle)

# 在串列尾端新增元素
motorcycle.append('honda')
print(motorcycle)

# 在空串列中新增元素

motorcycle = []

motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('suzuki')

print(motorcycle)

# 在串列中插入元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 使用del陳述句刪除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# #使用del陳述句刪除之後就不能存取

# 使用 pop()方法刪除
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# 彈出串列中任一位置的項目
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# 依據數值來刪除項目
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# 加入變數
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)

print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
