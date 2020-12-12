#necessary imports 
import time
import tkinter as tk
import random
import web_blocker


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
    Welcome to the DisConnect !
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
        quote_filer=open("quotes.csv","r+")
        quote_data=quote_filer.read()
        quote_data_sep=quote_data.split("&")
        quote_count=len(quote_data_sep)
        quoter["text"]=quote_data_sep[random.randint(0,quote_count-1)]
        quoter.after(20000,changer)
    win=tk.Tk()
    fbvar=tk.IntVar()
    igvar=tk.IntVar()
    rdvar=tk.IntVar()
    twvar=tk.IntVar()
    win.title("DisConnect")
    win.geometry("1920x720")
    win.configure(bg='black')
    #quote=tk.StringVar()
    quoter=tk.Label(win,text="Welcome to Project DisConnect",bg="black",font=("Courier", 17),fg="SpringGreen")
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




    quoter.after(5000,changer)
    win.mainloop()


if __name__ == "__main__":
    eula()