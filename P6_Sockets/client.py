import socket

PACKET_SIZE = 1024
ENCTYPE = 'utf-8'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = input("Enter server address: ")
server_port = int(input("Enter server port: "))

client_socket.connect((server_address, server_port))

while True:
	message = input("Enter your message: ")
	encoded_message = message.encode(ENCTYPE)
	client_socket.send(encoded_message)
	reply = client_socket.recv(PACKET_SIZE)
	decoded_reply = bytes.decode(reply, ENCTYPE)
	print(f"Server: {decoded_reply}")