import socket
import logging
import os

LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"

# On check si le dossier existe et sinon on le créé
if not os.path.exists('/var/log/bs_server'):
    os.mkdir('/var/log/bs_server')

logging.basicConfig(filename="/var/log/bs_server/bs_server.log", format=LOG_FORMAT,
                    level=logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(level=logging.ERROR)
handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
logging.getLogger().addHandler(handler)

# On définit l'adresse IP et le port du serveur
host = '192.168.64.37'  # Écoute sur toutes les interfaces
port = 13337  # Port utilisé par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Association du socket à une adresse et un port
s.bind((host, port))

# Mise en écoute du socket
s.listen()

logging.info(f"Serveur en écoute sur {host}:{port}.")

# Attente d'une connexion
conn, addr = s.accept()
logging.info(f"Connexion établie avec {addr}.")

# Réception des données du client
data = conn.recv(1024)

# Interprétation de la chaîne comme une opération arithmétique
try:
    result = eval(data.decode('utf-8'))
    logging.info(f"Opération arithmétique reçue du client : {data.decode('utf-8')}")
    logging.info(f"Résultat du calcul : {result}")
except Exception as e:
    logging.error(f"Erreur lors de l'évaluation de l'opération arithmétique : {e}")
    result = "Erreur lors de l'évaluation de l'opération arithmétique."

# Envoi de la réponse au client
conn.sendall(str(result).encode('utf-8'))

# Fermeture de la connexion
conn.close()

# Fermeture du socket
s.close()


