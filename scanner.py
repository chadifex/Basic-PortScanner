import socket

IP_ADDRESS = input('Enter ip address: ')
x = int(input('Enter port starting range: '))
y = int(input('Enter port ending range: '))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    for port in range(x,y):
        try: # tries to do otherwise goes to next (doesnt die if failed)
            s.connect((IP_ADDRESS, port))
            print(f'port {port} is open and listening')
        except: #exception of try
            print(f'port {port} is closed')