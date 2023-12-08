import socket
import multiprocessing

PORT = 13579
PACKET_SIZE = 1024
ENCTYPE = 'utf-8'

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind(('127.0.0.1', PORT))

# client_socks: list[tuple[socket.socket, str]] = []

server_sock.listen()
(client_sock, addr) = server_sock.accept()


def accept_incoming_requests():
	while True:
		# (incoming_sock, addr) = server_sock.accept()
		# client_socks.append((incoming_sock, addr))
		pass


def listen_for_messages():
	while True:
		for sock in client_socks:
			(client_sock, address) = sock
			print(f"Listening for data from {address}")
			recv_data = client_sock.recv(1024)
			decoded_data = bytes.decode(recv_data, ENCTYPE)
			print(f"{address}: {decoded_data}")


try:
	while True:
		recv_data = client_sock.recv(1024)
		decoded_data = bytes.decode(recv_data, ENCTYPE)
		ip, port = addr
		print(f"{ip}:{port} - {decoded_data}")
		# reply = input("Enter a reply: ")
		reply = str(eval(decoded_data))
		encoded_reply = reply.encode(ENCTYPE)
		client_sock.send(encoded_reply)
except Exception as e:
	print(e)
	client_sock.close()
	server_sock.close()


# handler_thread = multiprocessing.Process(target=accept_incoming_requests)
# listener_thread = multiprocessing.Process(target=listen_for_messages)
#
# handler_thread.start()
# listener_thread.start()
