from tkinter import *
from gtts import gTTS
import speech_recognition as sr
import os

root=Tk()                           #window created
root.geometry("1000x800")            #set width and height
#root.resizable(0,0)                 #set fixed size of window
root.title("LET'S SAY SOMETHING")   #set title



frame1=Frame(root,bg="LightPink",height="200")              #making background stylish
frame1.pack(fill=X)                #place the widget in GUI window

frame2=Frame(root,bg="grey",height="300")
frame2.pack(fill=X)

frame3=Frame(root,bg="skyblue",height="300")
frame3.pack(fill=X)

heading= Label(frame1,text ="LETS'S SAY SOMETHING ", font="Baskerville 16 bold")
heading.place(x=350,y=100)

label1=Label(frame2,text="TEXT TO SPEECH ",font="Baskerville 16 bold")
label1.place(x=400,y=50)

label2=Label(frame3,text="SPEECH TO TEXT",font="Baskerville 16 bold")
label2.place(x=400,y=40)

label3=Label(frame3,text="you said :",font="Baskerville 10 bold")
label3.place(x=200,y=140)

entry=Entry(frame2,width=50,bd=4,font=14)
entry.place(x=280, y=100)
entry.insert(0," ")



#.................function for text to speech conversion.........
def txt_speech():
    language="en"
    Output = gTTS(text=entry.get(), lang=language, slow=False)
    Output.save("Output.mp3")
    os.system("Output.mp3")

#......................function for speech to text conversion..........
pass_str=StringVar()                 #stores the text
def speech():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something......")
        audio =r.listen(source)
        a=r.recognize_google(audio)
        pass_str.set(a)

#..................function for copy text from speech to text............

btn=Button(frame2,text="CONVERT",command=txt_speech,bg="black",fg="white",bd=3,pady=5,width=10)
btn.place(x=450,y=150)

btn2=Button(frame3,text="CONVERT",command=speech,bg="black",fg="white",bd=3,pady=5,width=10)
btn2.place(x=450,y=80)

entry1=Entry(frame3,textvariable=pass_str,width=80)
entry1.place(x=300,y=140)

root.mainloop()
