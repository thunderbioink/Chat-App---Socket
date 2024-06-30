# Import requried modules
import socket
import threading


HOST = '127.0.0.1'
PORT = 2456 # use any port between 0 to 65535
LISTENER_LIMIT = 5
active_clients = [] #List of all connected users


# Method that sends new messages to all clients that are
# connected currently to this server:
def send_messages_to_all(from_username, message):
    pass


# Method to handle client:
def handle_client(client):
    
    # Server will isten for lcient message that will
    # Contain the username:
    while True:
        
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            
        else:
            
            print('Client username is empty')
    
    


# Main Method:
def main():
    # Create socket class object:
    # IPv4 addresses == AF_INET: 
    # TCP vs UDP:implementing TCP in SCOK_STREAM. For UDP use SOCK_DGRAM
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Create a try catch_block:
    try:
        # Provide serverr with address in form of host IP & port
        # Bind Host and Port
        server.bind((HOST, PORT))
        print(f'Server is running on {HOST} {PORT} 🌟')
    except Exception as e:
        print(f'Unable to bind to host "{HOST}" and port "{PORT}" :c ')
        print(e)
        return
        
    # Set server limit:
    # Only add up to five connections at a time:
    server.listen(LISTENER_LIMIT)
    
    # WHILE loop will keep listening for client connections:
    while True:
        client, address = server.accept()
        print(f'Successful connection to client {address[0]} {address[1]} c:')
        
        threading.Thread(target=handle_client, args=(client, )).start()
    

if __name__ == '__main__':
    
    main()