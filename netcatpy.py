import socket

target_socket = "0.0.0.0"
taget_port = 9942

target_meUDP = "127.0.0.1"
target_portUDP = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_socket,taget_port))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)
print(response.decode())
client.close()

client_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_UDP.sendto(b"AAAABBBBCCC",(target_meUDP, target_portUDP))

data, addr = client_UDP.recvfrom(4096)

print(data.decode())
client_UDP.close()