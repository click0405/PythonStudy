#   3. 从凌晨0:0:0 计时，到现在已经过了63320秒
#     请问，现在是几时，几分，几秒,写程序打印出来
#     (提示: 可以用地板除和求余实现)

s = 63320  # 秒
hour = s // 60 // 60    # 计算小时
minute = s % 3600 // 60  # 计算分钟
second = s % 60  # 秒
print("时间是", hour, ':',
               minute, ':',
               second)
