from socket import *
import os


serverName = '127.0.0.1'
serverPort = 12000

# filename = "file.txt"
archivo = "D:/ITSC/REDES/Laboratorios/Redes2021MCapeletti/carpeta/a.txt"
filename = "D:/ITSC/REDES/Laboratorios/Redes2021MCapeletti/carpeta/a.txt"
one_conection_only = (True)

def createSocket(serverAdress, serverPortt):
# AF_INET establece como protocolo de red a IP
# SOCK_STREAM establece como protocolo de transporte a TCP
		serverSocket = socket(AF_INET, SOCK_STREAM)

		serverSocket.bind((serverAdress,serverPortt))

		serverSocket.listen(1)
		print('The server is ready to receive')

		return serverSocket

severSocket = createSocket(serverName, serverPort)


def switch(cap):

    if cap == "LIST":
        valor =  os.listdir()
        convert =  str(valor)
        return convert 

    # elif sentence == "GET":
    #     with open("readfile.txt","wb") as file:
    #         print("archivo abierto")
    #         print("recibiendo datos...")
    #         while 1:
    #             data=clientSocket.recv(1024)
    #             print(f"data = {data!r}")
    #             if not data:
    #                 break
    #             file.write(data)
    #             return data    

    elif cap == "METADATA":       
        valor =  os.stat(archivo)
        convert = str(valor)
        return convert 
        #s

    elif cap == "CLOSE":
        connectionSocket.close()
         
        

    else:
       return capitalizedSentence

#a
connectionSocket, addr = severSocket.accept()

while 1:
	

	print("Se estableció la conexion")

	print(addr)

	sentence = connectionSocket.recv(1024)
	
	capitalizedSentence = sentence.decode().upper()



	capitalizedSentence = switch(capitalizedSentence)


	
	connectionSocket.send(capitalizedSentence.encode())

	#connectionSocket.close()


# 	with open(filename, "rb") as file:
# 		data = file.read(1024)
# 		while data:
# 			connectionSocket.send(data)
# 			print(f"enviando {data!r}")
# 			data = file.read(1024)
# 	print("enviado correctamente")
# 	sentence = connectionSocket.receive_file()
# 	if (one_conection_only):
# 		break
# socket.shutdown(1)

# sentence.write(sentence)