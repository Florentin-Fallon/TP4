import socket
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', action='store')
args = parser.parse_args()

if args.port:
    if int(args.port) not in range(0, 65535):
        print(f"ERROR Le port spécifié n'est pas un port possible (de 0 à 65535)")
        exit(1)

    if int(args.port) < 1024:
        print(f"ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
        exit(1)

host = ''
port = 13337 if not args.port else int(args.port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
conn, addr = s.accept()
print(f"Un client vient de se co et son IP c'est {addr}")

while True:

    try:
        data = conn.recv(1024)
        if not data: break
        print(f"Données reçues du client : {data}")

        data_str = str(data)

        if "meo" in data_str:
            conn.sendall(bytes('Meo à toi confrère.', 'utf-8'))
        elif "waf" in data_str:
            conn.sendall(b'ptdr t ki')
        else:
            conn.sendall(b'Mes respects humble humain.')

    except socket.error as e:
        print(f"Error : {e}")
        break

conn.close()
sys.exit(0)