from socket import AF_INET, socket, SOCK_STREAM ,gaierror
from threading import Thread
import tkinter
import sys

def receive(): #function for recieving messages and displying them
    while True:
        try:
            msg = client_socket.recv(msglen).decode("utf8")
            msg_list.insert(tkinter.END, msg)
            if msg == "/end":
                client_socket.close()
                chatroom.quit()
        except OSError:  
            break


def send(event=None): #function for sending the messages
    msg = my_msg.get()
    my_msg.set("") 
    client_socket.send(bytes(msg, "utf8"))
    if msg == "/q":
        client_socket.close()
        chatroom.quit()


def on_closing(event=None):#ending the chatroom for this client
    my_msg.set("/q")
    send()


#all specifics regarding the GUI
chatroom = tkinter.Tk()
chatroom.title("ChatRoom")

messages_frame = tkinter.Frame(chatroom)
my_msg = tkinter.StringVar()    # For the messages to be sent.
my_msg.set("")                  #to keep the input empty
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
#sizes and locations of the GUI
msg_list = tkinter.Listbox(messages_frame, height=20, width=60, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(chatroom, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(chatroom, text="Send", command=send)
send_button.pack()

chatroom.protocol("WM_DELETE_WINDOW", on_closing)

#a try except to make sure the user did not leave out any fields
try:
    HOST = sys.argv[2]
    PORT = sys.argv[3]
    PORT = int(PORT)
    name = sys.argv[1]
except IndexError:
    print("you have not entered all 3 required values")
    sys.exit()

msglen = 78
ADDRESS = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
#to make sure that the user did not enter an invalid port number/address
try:
    client_socket.connect(ADDRESS)
    client_socket.send(bytes(name, "utf8"))

    receive_thread = Thread(target=receive)
    receive_thread.start()
    tkinter.mainloop() 
#terminates if error is found
except (ConnectionRefusedError, gaierror):
    print("Incorrect Address or Port")
    sys.exit()

