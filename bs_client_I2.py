from sys import exit
import socket

host = '192.168.64.37'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    s.connect((host, port))
    input("Que veux-tu envoyer au serveur :")
except:
    print("On dirait qu'il y a eu un soucis, déso.")


s.sendall(b'Meooooo !')
data = s.recv(1024)
s.close()
print(f"Le serveur a répondu {repr(data)}")
exit(0)