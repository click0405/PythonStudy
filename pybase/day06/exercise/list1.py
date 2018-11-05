# 练习:
#   已知有列表:
#     L = [3, 5]
#     用索引的切片等操作,将原列表的改变为:
#     L = [1, 2, 3, 4, 5, 6]
#     将列表反转(先后顺序颠倒),删除最后一个元素后,打印此列表:
#        print(L) # [6, 5, 4, 3, 2]
    

L = [3, 5]
# print(id(L))
L[1:1] = [4]
L[0:0] = [1, 2]
L[len(L):len(L)] = [6]
print(L)  # L = [1, 2, 3, 4, 5, 6]

# 将列表反转(先后顺序颠倒),删除最后一个元素后,打印此列表:
L[::] = L[::-1]  # 新建的列表,重新赋值给L
del L[-1]
print(L) # [6, 5, 4, 3, 2]
# print(id(L))  # 会变化吗?
