#/usr/bin/env python3
#coding=utf-8
from socket import *
from threading import Thread
import re
from settings import *

class HTTPServer():
	def __init__(self, address):
		self.address = address
		self.create_socket()
		self.bind(address)

	def create_socket(self):
		self.sockfd = socket()
		self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	
	def bind(self, address):
		self.ip = address[0]
		self.port = address[1]
		self.sockfd.bind(address)

	
	def start(self):
		print(u'开启http服务,等待客户端连接.....')
		self.sockfd.listen(5)
		while True:
			connfd, addr = self.sockfd.accept()
			print(addr, '已经连接')
			http_client = Thread(target=self.handle, args=(connfd, ))
			http_client.setDaemon(True)
			http_client.start()
	def handle(self, connfd):
		request = connfd.recv(4096)
		if not request:
			connfd.close()
			return
		request_lines = request.splitlines()
		request_line = request_lines[0].decode('utf-8')
		pattern = r'(?P<METHOD>[A-Z]+)\s+(?P<PATH_INFO>/\S*)'
		try:
			env = re.match(pattern, request_line).groupdict()			
			print(env)
			
			response_headers = 'HTTP/1.1 200\r\n'
			response_headers += '\r\n'
			response_body = 'Server success'
			response = response_headers + response_body
			connfd.send(response.encode())
			connfd.close()
		except:
			response_headers = 'HTTP/1.1 500 Server Error!\r\n'
			response_headers += '\r\n'
			response_body = 'Server Error!'
			response = response_headers + response_body
			connfd.send(response.encode())


if __name__ == '__main__':
	httpfd = HTTPServer(ADDR)
	httpfd.start()
	
