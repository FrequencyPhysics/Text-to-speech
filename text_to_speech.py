from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("300x300")
root.config(bg="lightblue")

msg = StringVar()
gh = Entry(root,textvariable=msg,width=45,bg="lightblue")
gh.place(x=10,y=50)
l1 = Label(root,text="TEXT TO SPEECH",font=("Arial",15),bg="lightblue",fg="white")
l1.pack(side=TOP)

def text_to_speech():
    message = gh.get()
    speech=gTTS(text=message)
    speech.save('ade.mp3')
    playsound('ade.mp3')

def exit():
    root.destroy()

def reset():
    msg.set("")

b1 = Button(root,text="PLAY",command=text_to_speech,font=(15),bg="lightblue",fg="white")
b1.place(x=5,y=100)

b2 = Button(root,text="EXIT",command=exit,font=(15),bg="lightblue",fg="white")
b2.place(x=85,y=100)

b3 = Button(root,text="RESET",command=reset,font=(15),bg="lightblue",fg="white")
b3.place(x=160,y=100)

root.mainloop()