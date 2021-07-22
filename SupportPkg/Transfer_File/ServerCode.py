import socket
import tqdm
import os
# device's IP address
SERVER_HOST = "192.168.225.221"
SERVER_PORT = 5001
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "+" #"<SEPARATOR>"

# create the server socket
# TCP socket
s = socket.socket()
# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))

# enabling our server to accept connections
# 5 here is the number of unaccepted connections that
# the system will allow before refusing new connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
# accept connection if there is any
client_socket, address = s.accept() 
# if below code is executed, that means the sender is connected
print(f"[+] {address} is connected.")

# receive the file infos
# receive using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
# remove absolute path if there is
filename = "Transfer\\Receive\\" + os.path.basename(filename) 
# convert to integer
filesize = int(filesize)


# start receiving the file from the socket
# and writing to the file stream
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    for _ in progress:
        # read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:    
            # nothing is received
            # file transmitting is done
            break
        # write to the file the bytes we just received
        f.write(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))

# close the client socket
client_socket.close()
# close the server socket
s.close()



#----------------------------------------------------------------------------------------#
"""
You can extend this code for your own needs now, here are some examples you can implement:

Enabling the server to receive multiple files from multiple clients in the same time using threads.
Compressing the files before sending them.
Encrypting the file before sending it, to ensure that no one has the ability to intercept and read that file, this tutorial will help.
Ensuring the file is sent properly by checking the checksums of both files (the original file of the sender and the sent file in the receiver). 
    In this case, you need secure hashing algorithms to do it.
"""
#----------------------------------------------------------------------------------------#



