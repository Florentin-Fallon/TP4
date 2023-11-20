import socket

host = ''
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    print(f"Un client vient de se co et son IP c'est {host}")
    s.connect((host, port))
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
except socket.error:
    print("On dirait qu'il y a eu un soucis, déso.")
    exit(1)

while True:

    try:
        # On reçoit 1024 bytes de données
        data = conn.recv(1024)

        # Si on a rien reçu, on continue
        if not data: break

        # On affiche dans le terminal les données reçues du client
        print(f"Données reçues du client : {data}")

        if data == 'meo':
            print("Meo à toi confrère")
        elif data == 'waf':
            print("ptdr t ki")
        else:
            print("Mes respects humble humain")

        # On répond au client un truc
        conn.sendall(b"Hi mate !")

    except socket.error:
        print("Error Occured.")
        break

# On ferme proprement la connexion TCP
conn.close()
