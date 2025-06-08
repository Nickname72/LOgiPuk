import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('local', 12345))

server_socket.listen(5)
print("Server is listening on port 12345...")

conection, address = server_socket.accept()
print(f"Connection from {address} has been established.")

connection.send(bytes("Welcome to server!", "utf-8"))
data = connection.recv(1024).decode("utf-8")

print(f"Received from client: {data}")
connection.send(bytes("Hello from the server!","utf-8"))

conection.close()
server_socket.close()



