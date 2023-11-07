from sys import exit
import socket

host = '192.168.64.37'  # IP du serveur
port = 13337             # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
s.connect((host, port))
# note : la double parenthèse n'est pas une erreur : on envoie un tuple à la fonction connect()

# Envoi de data bidon
s.sendall(b'Meooooo !')

# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(1024)

# On libère le socket TCP
s.close()

# Affichage de la réponse reçue du serveur
print(f"Le serveur a répondu {repr(data)}")

exit(0)