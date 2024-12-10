import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('127.0.0.1', 65432))  # Server IP and port

    # Send a message to the server
    client_socket.sendall("ping".encode())

    # Receive a response from the server
    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")

    # Close the connection
    client_socket.close()

# Run the client
start_client()
