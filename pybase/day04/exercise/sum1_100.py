#   1. 写程序, 计算:
#     1 + 2 + 3 + 4 + ..... 100 的和
#     并打印结果
#     提示:  用一个专用的变量初始化为零,用它来保存和

s = 0  # 此变量用来记录每个加后的结果
i = 1
while i <= 100:
    # print(i)
    s = s + i  # s += i
    i += 1

print("和是:", s)