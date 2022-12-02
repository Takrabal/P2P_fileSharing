from cProfile import label
from curses import window
from tkinter import *
import socket
from tkinter import filedialog
import os

root =Tk()
root.title("ShareFile")

root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)

def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
        title='select Image File',
        filetypes =( ('file_type', '*.txt'),('all files','*.*') ) )

    def sender():
        s=socket.socket()
        host=socket.gethostbyname(socket.gethostname())
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print("waiting for any incoming connections...")
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("File and Data has been transmitted successfully..")
        

    #icon
    image_icon = PhotoImage(file = "Image/shareit.png")
    window.iconphoto(False,image_icon)

    Sbackground = PhotoImage(file = "Image/background.png")
    Label(window,image=Sbackground).place(x=-2,y=0)

   
    Mbackground = PhotoImage(file = "Image/id.png")
    Label(window,image=Mbackground,bg="#f4fdfe").place(x=100,y=260)


    host=socket.gethostbyname(socket.gethostname())
    Label(window,text=f'ID: {host}', bg='white',fg='black').place(x=140,y=290)

    Button(window,text="+select file",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000", command=select_file).place(x=110,y=150)
    Button(window,text="Send",width=8,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=sender).place(x=300,y=150)




    window.mainloop() 

def Receive():
    main=Toplevel(root)
    main.title("Receive")
    main.geometry
    main.geometry("450x560+500+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)

    def receiver():
        ID=SenderId.get()
        filename1=incoming_file.get()

        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1, 'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("file has been received successfully")


    #icon
    image_icon = PhotoImage(file = "Image/shareit.png")
    main.iconphoto(False,image_icon)

    Rbackground = PhotoImage(file = "Image/receiver.png")
    Label(main,image=Rbackground).place(x=-4,y=0)

    logo= PhotoImage(file='Image/profile.png')
    Label(main,image=logo,bg="#f4fdfe").place(x=10,y=250)
    Label(main,text="Receiver",font=('arial', 20), bg="#f4fdfe").place(x=100,y=270)

    Label(main,text="Input sender id",font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20,y=340)
    SenderId= Entry(main,width=25,fg="black",border=2, bg='white',font=('arial',15) )
    SenderId.place(x=20,y=370)
    SenderId.focus()

    Label(main,text="filename for the incoming file",font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20,y=420)
    incoming_file= Entry(main,width=25,fg="black",border=2, bg='white',font=('arial',15) )
    incoming_file.place(x=20,y=450)

    rr=Button(main,text="Receive",compound=LEFT,width=10,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=500)    

    main.mainloop() 

#icon
image_icon = PhotoImage(file = "Image/shareit.png")
root.iconphoto(False,image_icon)

Label(root,text = "File Transfer",font=('Acumin Varia ble Concept',20,'bold'),bg = "#f4fdfe").place(x=20,y=30)

Frame(root,width=400, height=2, bg ="#f3f5f6").place(x=30,y=80)

send_image=PhotoImage(file="Image/send.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Send)
send.place(x=30,y=100)
 
Recv_image=PhotoImage(file="Image/receive.png")
Recv=Button(root,image=Recv_image,bg="#f4fdfe",bd=0, command=Receive)
Recv.place(x=300,y=100 )

Label(root,text = "Send",font=('Acumin Varia ble Concept',17,'bold'),bg = "#f4fdfe").place(x=65,y=200)
Label(root,text = "Receive",font=('Acumin Varia ble Concept',17,'bold'),bg = "#f4fdfe").place(x=300,y=200)

background = PhotoImage(file = "Image/background.png")
Label(root,image=background).place(x=-22,y=328)

root.mainloop()
  
