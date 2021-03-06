# 练习:
#   写一个函数 get_score() 来获取学生输入的成绩(0 ~ 100) 的数,如果用户输入的不是0~100的整数则返回0,否则返回输入的整数
#   如:
#     def get_score():
#         ...
#     score = get_score()
#     print("您输入的成绩是:", score)

# 方法2 在get_score函数内部加入try语句来进行错误处理
def get_score():
    try:
        s = int(input("请输入成绩(0~100): "))
    except ValueError:
        return 0

    if not (0 <= s <= 100):
        return 0
    return s

score = get_score()
print("您输入的成绩是:", score)

