from socket import *
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = input("Введіть ім'я:")
client_socket.connect(('localhost',12345))
client_socket.send(name.encode())

def send_mes():
    while True:
        cl_mes = input()
        if cl_mes.lower() == "exit":
            client_socket.close()
            break
    client_socket.send(cl_mes.encode())

threading.Thread(target=send_mes,daemon=True).start()

while True:
    try:
        message = client_socket.recv(1024).decode('utf-8').strip()
        if message:
            print(message)
    except Exception as e:
        print(f"An error occured: {e}")
        break

command = input('Введіть команду:')
client_socket.send(command.encode())
print(client_socket.recv(1024).decode())

response = client_socket.recv(1024).decode()
print(f'Відповідь від сервера: {response}')

client_socket.close()

