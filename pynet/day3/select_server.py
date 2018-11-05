from select import select 
from socket import * 

# 创建套接字作为关注的ＩＯ
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#添加到关注列表
rlist = [s]
wlist = []
xlist = [s]

while True:
    #ＩＯ监控
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        #如果r is s说明s就绪即有客户端发起链接
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)
        #某个客户端链接套接字就绪，接收消息
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print("收到:",data.decode())
            # r.send("收到消息".encode())
            wlist.append(r)

    for w in ws:
        w.send("收到消息".encode())
        wlist.remove(w)

    for x in xs:
        x.close()
        raise