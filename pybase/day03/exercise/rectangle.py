# 练习:
#   写一个程序,打印一个高度为4行的矩形方框
#   如:
#     请输入矩形宽度: 10
#   打印:
#     ##########
#     #        #
#     #        #
#     ##########

w = int(input("请输入矩形宽度: "))
# 方法1
print("#" * w)
print("#", ' ' * (w - 2), "#", sep='')
print("#", ' ' * (w - 2), "#", sep='')
print("#" * w)

# 方法2
# print("#" * w)
# print("#" + ' ' * (w - 2) + "#")
# print("#" + ' ' * (w - 2) + "#")
# print("#" * w)
