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


while 1:
    
    # data = receive_data(socket)
 
    sentence = input('Input lowercase sentence:')
    
    
    if sentence == "close":
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('From Server: ' + modifiedSentence.decode())
        clientSocket.close()
        print("usted cerro la conexion del cliente")
        break 
    
    else:
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('From Server: ' + modifiedSentence.decode()) 
    


        
    







