# 写程序,实在现以要求:
#   1. 将如下数据形成一个字典seasons:
#     键           值
#     1  ----> '春季有1,2,3月'
#     2  ----> '夏季有4,5,6月'
#     3  ----> '秋季有7,8,9月'
#     4  ----> '冬季有10,11,12月'

#   2. 让用户输入一个整数,代表季度,打印这个季度的信息,如果用户输入的信息不存在于字典内,则打印"信息不存在"

# 生成字典 方法1
# seasons = {}
# seasons[1] = '春季有1,2,3月'
# seasons[2] = '夏季有4,5,6月'
# seasons[3] = '秋季有7,8,9月'
# seasons[4] = '冬季有10,11,12月'

seasons = {
    1: '春季有1,2,3月',
    2: '夏季有4,5,6月',
    3: '秋季有7,8,9月',
    4: '冬季有10,11,12月'
}

print(seasons)

#   2. 让用户输入一个整数,代表季度,打印这个季度的信息,如果用户输入的信息不存在于字典内,则打印"信息不存在"
n = int(input("请输入一个整数: "))
if n in seasons:
    print(seasons[n])
else:  # n not in seasons
    print("信息不存在")
