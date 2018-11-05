from select import select 
from socket import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

#关注套接字ＩＯ
print("监控ＩＯ")
rs,ws,xs = select([s],[],[],3)
print("处理ＩＯ")
