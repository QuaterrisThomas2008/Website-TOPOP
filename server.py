import sqlite3
import hashlib
import socket
import threading


def handle_connection(c):
    try:
       print("Client connected")

       c.send("Username: ".encode())
       username = c.recv(1024).decode().strip()
       print(f"Received username: {username}")
       c.send("Password: ".encode())
       password = c.recv(1024).decode().strip()
       print(f"Received password (pre-hash): {password}")
       password = hashlib.sha256(password.encode()).hexdigest()
       print(f"Hashed password: {password}")
       conn = sqlite3.connect("userdata.db")
       cur = conn.cursor()
       cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
       if cur.fetchall():
         c.send("Login Successfully!".encode())
         print("Login successful")
       else:
          c.send("Login Failed! WOMP WOMP".encode())
          print("Login failed")
        
          conn.close()
    except Exception as e:
       print(f"Error: {str(e)}")
       c.send(f"Error: {str(e)}".encode())

    finally:
       c.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 3333))
server.listen()
print("Server started on port 3333...")

while True:
   client, addr=server.accept()
   threading.Thread(target=handle_connection, args=(client,)).start()



