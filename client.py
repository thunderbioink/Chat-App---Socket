# Import modules:
import socket
import threading

HOST = '127.0.0.1' 
PORT = 2456

# Main method:

def main():
    
    # Create socket object:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to server:
    try:
        client.connect((HOST, PORT))
        print(f'Successfully connected to server c: 🌟')
        
    except:
        print(f'Unable to connect to server {HOST} {PORT}')
    
if __name__ == '__main__':
    
    main()