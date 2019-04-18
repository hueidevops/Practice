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
    print(u"Hi " + customer[i].title() + "，邀請您參加本次餐會。")
    i += 1

print(u"\n我找到更大的餐桌了，再多邀請三位來賓一起來參加吧！")

new_customer1 = "timo"
new_customer2 = "jackal"
new_customer3 = "irene"

customer.insert(0, new_customer1)
customer.insert(2, new_customer2)
customer.append(new_customer3)

i = 0
while i < 9:
    print(u"哈囉 " + customer[i].title() + ", 邀請您參加本次餐會。")
    i += 1
