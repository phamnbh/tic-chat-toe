import socket
import sys

class server():
	def __init__(self):
		self.host = ""
		self.port = 1234
		self.socket = None
		self.data = None

	def create_socket(self):
		try:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error as msg:
			print ('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
			sys.exit();

		print("Socket Created")

	def bind_socket(self):
		try:
			self.socket.bind((self.host, self.port))
		except socket.error as msg:
			print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
			sys.exit()
		
		print("Socket bind complete")

	def listen_receive(self):
		self.socket.listen(10)

		print("Listening...")

		conn, addr = self.socket.accept()

		print('Connected with ' + addr[0] + ':' + str(addr[1]))

		self.data = conn.recv(1024)

	def print_rinfo(self):
		print(self.data.decode("utf-8"))

	def run(self):
		self.create_socket()
		self.bind_socket()
		self.listen_receive()
		self.print_rinfo()

class client():
	def __init__(self):
		self.remote_ip = "192.168.0.16"
		self.port = 8888
		self.socket = None

	def create_socket(self):
		try:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error as msg:
			print ('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
			sys.exit();

		print("Socket Created")

	def connect(self):
		self.socket.connect((self.remote_ip, self.port))
		print ('Socket Connected to ' + self.remote_ip + ' on ip ' + self.remote_ip)

	def send_data(self):
		message = input("Type message here")
		self.socket.sendall(message.encode())

	def print_recvdata(self):
		print(self.socket.recv(1024).decode("utf-8"))

	def run(self):
		self.create_socket()
		self.connect()
		self.send_data()
		self.print_recvdata()



if __name__ == '__main__':
	a = input("client or server?")
	if a == 'c':
		b = client()
		b.run()
		c = input()
	elif a == 's':
		b = server()
		b.run()
		c = input()


