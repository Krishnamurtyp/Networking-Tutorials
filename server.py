import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to an address and port
    server_socket.bind(('127.0.0.1', 65432))  # IP and port

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening...")

    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive data from the client
        data = client_socket.recv(1024).decode()
        print(f"Received from client: {data}")

        # Send a response
        if data.lower() == "ping":
            client_socket.sendall("pong".encode())

        # Close the client socket
        client_socket.close()

# Run the server
start_server()
