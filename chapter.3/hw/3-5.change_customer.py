customer = ['charles', 'valerie', 'jason', 'ben', 'jasper', 'andy']

print(customer)

i = 0
while i < 6:
    # u -> 輸出中文
    print(u"Hi " + customer[i].title() + ", 要不要一起來吃個飯呢？")
    i += 1

cannot_arrive = 'jasper'
print(u"各位抱歉, " + cannot_arrive.title() + "有事無法參加本次餐會。")

customer.remove(cannot_arrive)

new_customer = 'vicky'
customer.append(new_customer)

i = 0
while i < 6:
    print(u"Hi " + customer[i].title() + "，邀請各位參加本次餐會。")
    i += 1
