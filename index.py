from tkinter import *
import os
def restart():
    os.system("shutdown -r -t 1")
def restart_time():
    os.system("shutdown -r -t 20")
def shutdown():
    os.system("shutdown -s -t 1")


st = Tk()
st.title("RESTART APP")
st.geometry("500x500")
st.configure(bg='black')
#restart
r_button = Button(st,text="RESTART",font=("arial",30,"bold"),bg="#E50914",cursor="plus",command=restart)
r_button.place(x=150,y=60,width=250 ,height=50)
#restart_beforetime
r_button = Button(st,text="Time Restart",font=("arial",30,"bold"),bg="red",cursor="plus",command=restart_time)
r_button.place(x=150,y=170,width=250 ,height=50)
#shutdown
r_button = Button(st,text="SHUT DOWN",font=("arial",30,"bold"),bg="red",cursor="plus",command=shutdown)
r_button.place(x=150,y=280,width=250 ,height=50)
#close
r_button = Button(st,text="close",font=("arial",30,"bold"),bg="red",cursor="plus",command=st.destroy)
r_button.place(x=150,y=370,width=250 ,height=50)

st.mainloop()