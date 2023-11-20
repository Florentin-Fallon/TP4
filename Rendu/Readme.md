# I. Simple bs program

# 1. First steps

# 🌞 bs_server_I1.py
# 🌞 bs_client_I1.py

Voici les résultats pour les 2 premier soleil :

Voici le résultat quand le client ce connecte :

```shell
[fallonflorentin@localhost TP4]$ python3 bs_client_I1.py 
Le serveur a répondu b'Hi mate !'
```

Voici le résultat sur le serveur :

```shell
[fallonflorentin@localhost TP4]$ python3 bs_server_I1.py 
Connected by ('192.168.64.38', 53158)
Données reçues du client : b'Meooooo !'
```

# 🌞 Commandes...

Voici les étapes pour la réalisation du serveur et du client sur les VM :

Installation de ***Git*** :

```shell
[fallonflorentin@localhost TP4]$ sudo dnf install git
```

Voici le clone du repo sur les 2 VM :

```shell
[fallonflorentin@localhost ~]$ git clone https://github.com/Florentin-Fallon/TP4.git
Cloning into 'TP4'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 6 (delta 0), reused 6 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.
```

Installation de python sur les VM :

```shell
[fallonflorentin@localhost ~]$ sudo dnf install python3
Upgraded:
  python-unversioned-command-3.9.16-1.el9_2.2.noarch                            
  python3-3.9.16-1.el9_2.2.aarch64                                              
  python3-libs-3.9.16-1.el9_2.2.aarch64                                         

Complete!
```

Ouverture du port 13337 sur les 2 VM :

```shell
[fallonflorentin@localhost TP4]$ sudo firewall-cmd --add-port=13337/tcp --permanent
```

Voici la liste pour bien voir que le port et bien ouvert :

```shell
[fallonflorentin@localhost TP4]$ sudo firewall-cmd --list-all
[sudo] password for fallonflorentin: 
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s1
  sources: 
  services: cockpit dhcpv6-client ssh
  ports: 13337/tcp
  protocols: 
  forward: yes
  masquerade: no
  forward-ports: 
  source-ports: 
  icmp-blocks: 
  rich rules: 
```
Redémarrage pour que les modifications prennent effet sur les VM :

```shell
[fallonflorentin@localhost TP4]$ sudo firewall-cmd --reload
```

Lancement du fichier bs_server_I1.py sur la VM serveur :

```shell
[fallonflorentin@localhost TP4]$ python3 bs_server_I1.py 
```

Lancement du fichier bs_client_I1.py sur la VM client :

```shell
[fallonflorentin@localhost TP4]$ python3 bs_client_I1.py 
```

Voici les fichiers avec le code qu'il faut pour le côté serveur :

[bs_server_I1.py](bs_server_I1.py)

De même pour le côté client :

[bs_client_I1.py](bs_client_I1.py)

Voici la commande ss avec le grep demander :

```shell
[fallonflorentin@localhost TP4]$ ss -lapute | grep 13337
tcp   LISTEN 0      1                   0.0.0.0:13337       0.0.0.0:*      users:(("python3",pid=12608,fd=3)) uid:1000 ino:37122 sk:2f cgroup:/user.slice/user-1000.slice/session-4.scope <->
```

# 2. User friendly

# 🌞 bs_client_I2.py

* retour visuel

Voici le message client quand il se connecte au serveur :

```shell
[fallonflorentin@localhost TP4]$ python3 bs_client_I2.py
Connecté avec succès au serveur 192.168.64.37 sur le port 13337
Que veux-tu envoyer au serveur :waf
Le serveur a répondu b'ptdr t ki'
```

Voici le "Que veux-tu envoyer au serveur" :

```shell
[fallonflorentin@localhost TP4]$ python3 bs_client_I2.py
Connecté avec succès au serveur 192.168.64.37 sur le port 13337
Que veux-tu envoyer au serveur :
```

Voici le fichier avec la configue du ***client*** :

[bs_client_I2.py](bs_client_I2.py)

# 🌞 bs_server_I2.py

* retour visuel

Voici le message client quand il se connecte au serveur :

```shell
[fallonflorentin@bsserver TP4]$ python3 bs_server_I2.py
Un client vient de se co et son IP c'est 192.168.64.38
Données reçues du client : waf
```

* réponse adaptative

Voici la configue pour la réponse adaptative :

```shell
if ('meo' in data.decode("utf-8")):
            conn.sendall("Meo à toi confrère.".encode("utf-8"))
        elif ('waf' in data.decode("utf-8")):
            conn.sendall("ptdr t ki".encode("utf-8"))
        else:
            conn.sendall("Mes respects humble humain".encode("utf-8"))
```

Voici le fichier avec toute la configue du ***serveur*** :

[bs_serveur_I2.py](bs_serveur_I2.py)

# 3. You say client I hear control

# 🌞 bs_client_I3.py

* vérifier que...

```shell
[fallonflorentin@localhost TP4]$ python3 bs_client_I3.py
Connecté avec succès au serveur 192.168.64.37 sur le port 13337
Que veux-tu envoyer au serveur :salut
Traceback (most recent call last):
  File "/home/fallonflorentin/TP4/bs_client_I3.py", line 19, in <module>
    raise ValueError("Le message doit contenir meo ou waf.")
ValueError: Le message doit contenir meo ou waf.
```

Voici le fichier :

[bs_client_I3.py](bs_client_I3.py)


# II. You say dev I say good practices

# 1. Args

# 🌞 bs_server_II1.py




# 2. Logs
# A. Logs serveur

# 🌞 bs_server_II2A.py

# B. Logs client
# 🌞 bs_client_II2B.py