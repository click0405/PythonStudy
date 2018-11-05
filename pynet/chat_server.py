#coding=utf-8
'''
Chatroom
env: python 3.5
socket and fork 
'''
from socket import *
import os,sys 

def do_login(s,user,name,addr):
    if (name in user)  or name == '管理员':
        s.sendto("该用户已存在".encode(),addr)
        return 

    s.sendto(b'OK',addr)

    #通知其他人
    msg = "欢迎 %s 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户加入ｕｓｅｒ
    user[name] = addr 

def do_request(s):
    # 存储结构　｛'zhangsan':('127.0.0.1',9999)｝
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        msgList = msg.decode().split(' ')
        #区分请求类型
        if msgList[0] == 'L':
            do_login(s,user,msgList[1],addr)

#创建网络链接
def main():
    ADDR = ('0.0.0.0',8888)   
    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    
    #用于接受各种客户端请求，调用相应的函数处理
    do_request(s)

if __name__ == "__main__":
    main()



