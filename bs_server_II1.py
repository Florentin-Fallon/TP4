import socket
import argparse

host = ''
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print(f"Un client vient de se co et son IP c'est {addr[0]}")
except socket.error:
    print("On dirait qu'il y a eu un soucis, déso.")
    exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, help='port number', default=13337)
parser.add_argument('-h','--help',action='help',default=argparse.SUPPRESS, help='show this help message and exit')

args = parser.parse_args()

if args.port < 0 or args.port > 65535:
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    exit(1)
elif args.port >= 0 and args.port <= 1024:
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    exit(2)
else:
    port = args.port


while True:

    try:
        # On reçoit 1024 bytes de données
        data = conn.recv(1024)

        # Si on a rien reçu, on continue
        if not data: break

        # On affiche dans le terminal les données reçues du client
        print(f"Données reçues du client : {data.decode('utf-8')}")

        if ('meo' in data.decode("utf-8")):
            conn.sendall("Meo à toi confrère.".encode("utf-8"))
        elif ('waf' in data.decode("utf-8")):
            conn.sendall("ptdr t ki".encode("utf-8"))
        else:
            conn.sendall("Mes respects humble humain".encode("utf-8"))

        # On répond au client un truc
        conn.sendall(b"Hi mate !")

    except socket.error:
        print("Error Occured.")
        break

# On ferme proprement la connexion TCP
conn.close()
