#necessary imports 
import time
import tkinter as tk
import random
import web_blocker
sites=[]
temp =3600
task_file=open("tasks.data","r")
task_data=task_file.read()
tasks=task_data.split(",")

def eula():
    def eula_destoyer():
        notice.destroy()
        agreee.destroy()
        eula.destroy()
        main_win()
        eula_file=open("eula.txt","w")
        eula_file.write("eula=True")    
    eula_file=open("eula.txt","r")
    eula_data=eula_file.read()
    if eula_data[5:]=="False":
        eula = tk.Tk()
        eula.title("Notice")
        eula.geometry("720x400")
        eula.configure(bg='black')
        notice=tk.Label(text='''Hello User,
    Welcome to the D!sConnect !
    By clicking the big button on the next page you'll be 
    blocking your access to social media sites until the 
    clock gets to zero (which'll be an hour afterwards)
    There'll be no way you'll be regain access to the 
    sites before the clock wants you to.
    So, we hope you're sporting enough to take on 
    our little challenge
    By agreeing you're pinky promising to join us
    in our grand venture to disconnect from the virtually
    and do something for yourself_''',font=("Courier", 15),bg="black",fg="SpringGreen")
        notice.grid(row=0+2,column=0) 
        agreee=tk.Button(text="Agree",command=eula_destoyer,font=("Courier", 11))
        agreee.grid(row=1+2,column=0)
        eula.mainloop()
    else:
        main_win()


def main_win():
    def changer():
        quote_filer=open("quotes.data","r+")
        quote_data=quote_filer.read()
        quote_data_sep=quote_data.split("&")
        quote_count=len(quote_data_sep)
        quoter["text"]=quote_data_sep[random.randint(0,quote_count-1)]
        quoter.after(20000,changer)
    def cntdwn():
        global temp
        global tasks
        dcbut["state"]="disabled"
        mins,secs = divmod(temp,60) 
        hours=0
        if mins >60:
            hours, mins = divmod(mins, 60)
            
        htim["text"]=hours
        mtim["text"]=mins
        stim["text"]=secs

        temp -= 1
        win.update()
        if temp%600==0:
            cheat["text"]='''Your task to get a 10 min cheat = '''+tasks[random.randint(0,len(tasks)-1)]
            win.update()
            cheatactivator["state"]="normal"
        if temp!=0:
            win.after(1000,cntdwn)
        else:
            web_blocker.unblock()
            dcbut["state"]="normal"
            cheat["text"]="Congrats"
            temp=3600
    def cheater():
        global temp
        temp=temp-600
        cheatactivator["state"]="disabled"

    def initiater():
        if fbvar.get()==1:
            web_blocker.block(["facebook.com"])
        if igvar.get()==1:
            web_blocker.block(["instagram.com"])
        if rdvar.get()==1:
            web_blocker.block(["reddit.com"])
        if twvar.get()==1:
            web_blocker.block(["twitter.com"])
        cntdwn()
    
    win=tk.Tk()
    fbvar=tk.IntVar()
    igvar=tk.IntVar()
    rdvar=tk.IntVar()
    twvar=tk.IntVar()
    win.title("D!sConnect")
    win.geometry("1920x720")
    win.configure(bg='black')
    #quote=tk.StringVar()
    quoter=tk.Label(win,text="Welcome to Project D!sConnect",bg="black",font=("Courier", 17),fg="SpringGreen")
    quoter.pack()
    #Checkboxes
    fb=tk.Checkbutton(text="Facebook",bg="black",fg="SpringGreen",font=("Courier", 15),variable=fbvar)
    fb.pack()
    fb.place(x=0,y=30)
    fb.toggle()
    ig=tk.Checkbutton(text="Instagram",bg="black",fg="SpringGreen",font=("Courier", 15),variable=igvar)
    ig.pack()
    ig.place(x=0,y=60)
    ig.toggle()
    rd=tk.Checkbutton(text="Reddit",bg="black",fg="SpringGreen",font=("Courier", 15),variable=rdvar)
    rd.pack()
    rd.place(x=0,y=90)
    rd.toggle()
    tw=tk.Checkbutton(text="Twitter",bg="black",fg="SpringGreen",font=("Courier", 15),variable=twvar)
    tw.pack()
    tw.place(x=0,y=120)
    tw.toggle()

    #Timer
    h=tk.StringVar()
    m=tk.StringVar()
    s=tk.StringVar()
    h.set("00")
    m.set("00")
    s.set("00")
    htim=tk.Label(text=00,bg="black",fg="SpringGreen",font=("Courier", 80))
    htim.pack()
    htim.place(x=650-60,y=300-80)
    mtim=tk.Label(text=00,bg="black",fg="SpringGreen",font=("Courier", 80))
    mtim.pack()
    mtim.place(x=800-60,y=300-80)
    stim=tk.Label(text=00,bg="black",fg="SpringGreen",font=("Courier", 80))
    stim.pack()
    stim.place(x=950-60,y=300-80)
    dcbut=tk.Button(text="D!sconnect",font=("Courier", 30),command=initiater)
    dcbut.pack()
    dcbut.place(x=640,y=500-80)

    #CheatMaker
    dividor=tk.Label(text="__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________",bg="black",fg="SpringGreen")
    dividor.pack()
    dividor.place(x=0,y=500)
    cheat=tk.Label(text="No tasks yet",bg="black",fg="SpringGreen",font=("Courier", 15))
    cheat.pack()
    cheat.place(x=20,y=520)
    cheatactivator=tk.Button(text="I did it",font=("Courier", 20),command=cheater)
    cheatactivator.pack()
    cheatactivator.place(x=1350,y=520)
    cheatactivator["state"]="disabled"



    quoter.after(5000,changer)
    win.mainloop()


if __name__ == "__main__":
    eula()