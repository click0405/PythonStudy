# 1. 输入一个整数,打印一个宽度和高度都是n个字符的长方形
#   如:
#     输入: 4
#   ####
#   #  #
#   #  #
#   ####
#     输入: 6
#   ######
#   #    #
#   #    #
#   #    #
#   #    #
#   ######

n = int(input('请输入宽度: '))
# 打印第一行
print("#" * n)

# 打印中间的 n - 2 行
i = 1
while i <= n - 2:
    print('#' + ' ' * (n - 2) + '#')
    i += 1

# 打印最后一行
if n > 1:
    print("#" * n)
