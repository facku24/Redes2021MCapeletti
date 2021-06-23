from socket import *
import os

serverName = '127.0.0.1'
serverPort = 12000

def createSocket(serverAdress, serverPortt):

    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((serverAdress,serverPortt))

    return clientSocket

# def switch():

#     sentence = input('Input lowercase sentence:')

#     if sentence == "LIST":
#         valor =  os.listdir()
#         convert =  str(valor)
#         return convert 

#     elif sentence == "GET":
#         with open("readfile.txt","wb") as file:
#             print("archivo abierto")
#             print("recibiendo datos...")
#             while 1:
#                 data=clientSocket.recv(1024)
#                 print(f"data = {data!r}")
#                 if not data:
#                     break
#                 file.write(data)
#                 return data    

#     elif sentence == "METADATA":       
#         valor =  os.stat(archivo)
#         convert = str(valor)
#         return convert 

#     elif sentence == "CLOSE":
#          clientSocket.close()
#          pass
        

#     else:
#        return sentence



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



