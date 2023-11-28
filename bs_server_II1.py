import socket
import argparse
import sys 

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

def parse_arguments():
    parser = argparse.ArgumentParser(description='Simple server with port handling.')

    parser.add_argument('-p', '--port', type=int, help='Specify the port to use. Must be an integer between 0 and 65535.')
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit.')

    return parser.parse_args()

def print_help():
    print("Usage: python bs_server_II1.py [-p PORT] [-h]")
    print("\nOptions:")
    print("  -p, --port Specify the port to use. Must be an integer between 0 and 65535.")
    print("  -h, --help Show this help message and exit.")
    sys.exit(0)

def main():
    args = parse_arguments()

    if args.help:
        print_help()

    if args.port is not None:
        if args.port < 0 or args.port > 65535:
            print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
            sys.exit(1)
        elif args.port <= 1024:
            print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au-dessus de 1024.")
            sys.exit(2)
        else:
            print(f"Utilisation du port spécifié : {args.port}")
    else:
        print("Utilisation du port par défaut : 13337")


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
