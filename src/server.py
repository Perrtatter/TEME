import socket

# Configuration
HOST = "localhost"  # Adresse locale
PORT = 4444        # Port d'écoute (doit être > 1024)

# Création du socket (IPv4, TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept() # Attend une connection   
    with conn:
        #print(f"Connecté par {addr}")
        while True:
            data = conn.recv(1024) # Reçoit 1024 octets max
            if not data:
                break
            print(f"Données reçues : {data.decode('utf-8')}")



input("Press [enter] to quit ...")