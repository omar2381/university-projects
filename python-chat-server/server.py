from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import sys

f = open("server.log","w") #resets the file for the first time
f.write("This is the beginning of the chatroom \n\n")
f.close()
#defining variables
clients = {}
addresses = {}
msglen = 1024

listofcommands=["/help: prints out list of commands",
                "/q: quits the chatroom                                                        ",
                "/list: shows the list of users                                                ", 
                "/msg: privately messages a user                                               ",      
                "/namech: changes your name                                                    ",
                "/end: terminates the server for all clients"]

#function to start up the server (for each individual client)
def start(port): 
    global SERVER
    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.bind(("127.0.0.1", int(port)))

#accepts clients attempting to connect (as long as the server is running)
def accept():
    while True:
        try:
            client, client_address = SERVER.accept()
            print("%s:%s has connected." % client_address) #prints connection message
            addresses[client] = client_address
            Thread(target=handle_client, args=(client,)).start()
        except OSError:
            sys.exit()

#function to write to the server log
def serverlog(msg):
    f = open("server.log","a")
    f.write(msg + "\n")
    f.close()

def handle_client(client):  # Takes client socket as argument.
    name = client.recv(msglen).decode("utf8")
    welcome = 'Welcome %s! enter /q to exit the chat or /help' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))

    serverlog(msg)

    clients[client] = name
    #loops as long as the user is connected and checks their messages for valid commands
    while True:
        try:
            msg = client.recv(msglen)

            if msg == bytes("/q", "utf8"): #quits the user, logs them leaving, and removes them from the list
                client.close()
                del clients[client]
                bye = "%s has left the chat." % name
                broadcast(bytes(bye, "utf8"))
                serverlog(bye)
                break
            
            elif msg == bytes("/help", "utf8"):#messages the user who requested the help command
                h = "/help"
                serverlog(h)
                for x in range(len(listofcommands)):
                    serverlog(listofcommands[x])
                    client.send(bytes(str(listofcommands[x]),"utf8"))

            elif msg == bytes("/list", "utf8"):#messages the user with the list of all connected users
                requester = client
                i = 1
                for client in clients:
                    var = clients[client]
                    car = str(i) + ". " + var
                    serverlog(car)
                    requester.send(bytes(str(i)+ ". " + var, "utf8"))
                    i = i + 1
                    
            elif msg == bytes("/msg", "utf8"):#section for the private message, the user enters /msg
                cart = " "
                requester = client
                siri = "enter the name of the user you want to message %s." % name#then must enter the name of the user they wish to message
                requester.send(bytes(siri, "utf8"))
                serverlog(siri)
                reciever = requester.recv(msglen)
                for clarify in clients:
                    if reciever.decode() == clients[clarify]:
                        siri = "enter the message you want to send to %s." %reciever.decode() #then must enter the message to be sent 
                        serverlog(siri)
                        requester.send(bytes(siri, "utf8"))
                        cart = clarify
                

                if cart == " ":
                    private = "you have entered an invalid username" #makes sure the user did not enter and invalid name
                    serverlog(private)
                    requester.send(bytes(private, "utf8"))
                else:
                    private = requester.recv(msglen).decode()
                    cart.send(bytes("private message from "+ name + ": "+ str(private), "utf8"))
                    serverlog("private message from "+ name + ": "+str(private))

            elif msg == bytes("/namech", "utf8"): #section to change the visiable username
                requester = client
                namech = "enter the name you want to have" + name
                serverlog(namech)
                requester.send(bytes(namech, "utf8"))
                newname = client.recv(msglen)
                serverlog(str(newname.decode()))
                for client in clients:
                    if name == clients[client]:
                        name = str(newname.decode())
                        clients[client] = newname.decode()

            elif msg == bytes("/end","utf8"):#section to terminate the program, and save the log
                serverlog("\n SERVERCLOSE \n")
                f.close()
                for client in clients: #if the user enters /end then the /end statement is send to all users and they are exited
                    client.send(bytes("/end","utf8"))
                SERVER.close()
                sys.exit()               
                
            else: #if the user did not enter any commands the message is sent to all
                serverlog(str(name) + ":" + str(msg.decode()))
                broadcast(msg, name + ": ")
        except (ConnectionResetError,ConnectionAbortedError):
            sys.exit()

def broadcast(msg, prefix=""):  
    for sock in clients:        # sends message to all clients
        sock.send(bytes(prefix, "utf8")+msg)

if __name__=="__main__": # main
    start(sys.argv[1])   # starts server
    SERVER.listen(10)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
    f.close()
    