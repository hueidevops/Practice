customer = ['charles', 'valerie', 'jason', 'ben', 'jasper', 'andy']

# print(customer)

i = 0
while i < 6:
    # u -> 輸出中文
    # print(u"Hi " + customer[i].title() + ", 要不要一起來吃個飯呢？")
    i += 1

cannot_arrive = 'jasper'
# print(u"各位抱歉, " + cannot_arrive.title() + "有事無法參加本次餐會。")

customer.remove(cannot_arrive)

new_customer = 'vicky'
customer.append(new_customer)

i = 0
while i < 6:
    # print(u"Hi " + customer[i].title() + "，邀請您參加本次餐會。")
    i += 1

# print(u"\n我找到更大的餐桌了，再多邀請三位來賓一起來參加吧！")

new_customer1 = "timo"
new_customer2 = "jackal"
new_customer3 = "irene"

customer.insert(0, new_customer1)
customer.insert(2, new_customer2)
customer.append(new_customer3)

i = 0
while i < 9:
    # print(u"哈囉 " + customer[i].title() + ", 邀請您參加本次餐會。")
    i += 1

print(u"大餐桌無法準時到貨，所以只能邀請兩位哦哦哦哦！")

j = 0
while j < 7:
    popped_customer = customer.pop()
    print(u"Hi " + popped_customer.title() + ", 您無法受邀來參加餐會哦！")
    j += 1

print("\n")

k = 0
while k < 2:
    last_customer = customer[k]
    print(u"Hi " + last_customer.title() + ", 請記得依約出席餐會哦！")
    k += 1

n = 0
while n < 2:
    del customer[0]
    n += 1

print(customer)




