from socket import *
import os
#d

serverName = '127.0.0.1'
serverPort = 12000

def createSocket(serverAdress, serverPortt):

    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((serverAdress,serverPortt))

    return clientSocket

clientSocket = createSocket(serverName, serverPort)

def envio():
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('From Server: ' + modifiedSentence.decode()) 

while 1:
    
    # data = receive_data(socket)
 
    sentence = input('Input lowercase sentence:')
    

    
    if sentence == "close":
        envio()
        clientSocket.close()
        print("se cerro la conexion del cliente")
        break 
    
    else:
        envio()
    


        
    







