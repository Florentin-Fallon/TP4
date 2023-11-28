import os
import socket
import sys
import re
import logging

LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"

# On check si le dossier existe et sinon on le créé
if not os.path.exists('/var/log/bs_client'):
    os.mkdir('/var/log/bs_client')

logging.basicConfig(filename="/var/log/bs_client/bs_client.log", format=LOG_FORMAT,
                    level=logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(level=logging.ERROR)
handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
logging.getLogger().addHandler(handler)

# On définit la destination de la connexion
host = '192.168.64.37'  # IP du serveur
port = 13337  # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
try:
    s.connect((host, port))
except Exception as e:
    logging.error(f"Impossible de se connecter au serveur {host} sur le port {port}.")
    exit(1)
# note : la double parenthèse n'est pas une erreur : on envoie un tuple à la fonction connect()

logging.info(f"Connexion réussie à {host}:{port}.")

accepted_regex = r'^([-+]?\d{1,6})\s*([-+*/])\s*([-+]?\d{1,6})$'

serv_input = input('Saisissez une opération arithmétique :')

if not re.match(accepted_regex, serv_input):
    logging.error(f"Le message {serv_input} n'est pas une opération arithmétique valide.")
    sys.exit(1)

s.sendall(bytes(serv_input, 'utf-8'))
logging.info(f"Message envoyé au serveur {host} : {serv_input}.")

# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(1024)

# On libère le socket TCP
s.close()

# Affichage de la réponse reçue du serveur
logging.info(f"Réponse reçue du serveur {host} : {data}.")

# On quitte proprement
sys.exit(0)