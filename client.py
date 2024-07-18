     import socket

def run_client():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", 3333))
        
        while True:
            message = client.recv(1024).decode()
            if not message:
                break
            client.send(input(message).encode())

        
        response = client.recv(1024).decide()
        print(response)
    except Exception as e:
        print(f"An error occurred:{e}")
    finally:
        client.close()

if __name__=="__main__":
    run_client()