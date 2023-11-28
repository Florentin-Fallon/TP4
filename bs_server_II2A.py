import os
import socket
import sys
import argparse
import logging

LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"

# On check si le dossier existe et sinon on le créé
if not os.path.exists('/var/log/bs_server'):
    os.mkdir('/var/log/bs_server')

logging.basicConfig(filename="/var/log/bs_server/bs_server.log", format=LOG_FORMAT,
                    level=logging.DEBUG)

# Pour afficher les logs dans la console
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter(LOG_FORMAT))
logging.getLogger().addHandler(handler)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', action='store', type=int)
args = parser.parse_args()

if args.port:
    if int(args.port) not in range(0, 65535):
        logging.error(f"Le port spécifié n'est pas un port possible (de 0 à 65535)")
        exit(1)

    if int(args.port) < 1024:
        logging.error(f"Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
        exit(1)

host = ''
port = 13337 if not args.port else int(args.port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

logging.info(f"Le serveur tourne sur {host}:{port}")

s.listen(1)
conn, addr = s.accept()
logging.info(f"Un client {addr} s'est connecté.")

while True:

    try:
        data = conn.recv(1024)
        if not data: break

        data_str = str(data)[:100]
        logging.info(f"Le client {addr} a envoyé {data_str}")

        resp = ""

        if "meo" in data_str:
            resp = 'Meo à toi confrère.'
        elif "waf" in data_str:
            resp = 'ptdr t ki'
        else:
            resp = 'Mes respects humble humain.'

        logging.info(f"Réponse envoyée au client {addr} : {resp}")
        conn.sendall(bytes(resp, 'utf-8'))

    except socket.error as e:
        print(f"Error : {e}")
        break

conn.close()
sys.exit(0)