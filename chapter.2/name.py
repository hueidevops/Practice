name = "ada lovelace"

# 首字大寫
print(name.title())

# 全部字母大寫
print(name.upper())

# 全部字母小寫
print(name.lower())

# 字串組合和連接
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)
print("Hello, " + full_name.title() + "!")

# 將組合字串加到變數中
msg = "Hello, " + full_name.title() + "!"
print(msg)

# 定位符號
print("\tPython")

# 換行符號
print("Languages:\nPython\nC\nJavaScript")

# 定位與換行
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 刪除字串右側空白
favorite_language = "python "
print(favorite_language.rstrip())

# 刪除空白字串後回存原變數
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)