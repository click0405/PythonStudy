from socket import *
import os,sys 

#创建套接字
def main():
    #从命令行输入服务器地址
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM) 
    
    while True:
        name = input("请输入姓名:")
        msg = "L " + name 
        #发送给服务端
        s.sendto(msg.encode(),ADDR)
        #等待回应
        data,addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break 
        else:
            print(data.decode())


if __name__ == "__main__":
    main()