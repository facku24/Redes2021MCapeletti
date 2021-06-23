from socket import *
import os

serverName = '127.0.0.1'
serverPort = 12000

def createSocket(serverAdress, serverPortt):

    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((serverAdress,serverPortt))

    return clientSocket




while 1:
    clientSocket = createSocket(serverName, serverPort)
    # data = receive_data(socket)
    # sentence = switch()

    sentence = input('Input lowercase sentence:')

    clientSocket.send(sentence.encode())

    # clientSocket.sendfile("F:\ITSC\3ERAÑO\Redes\TP1\Nuevacarpeta.txt")
    modifiedSentence = clientSocket.recv(1024)

    print('From Server: ' + modifiedSentence.decode())
    



# clientSocket.close()



