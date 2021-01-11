import tkinter as tk
from tkinter import Label,Entry
import os, _thread
    

def run_proc():
    
    os.system(r"D:\Kraya\2DNI\TP\Eval_Perfor\TP2_evalperform\prog\procexp.exe")

def para_window():

    win_2 = tk.Tk()
    win_2.title("Disk Banch paramétre")
    win_2.geometry("400x300")
    frame_2 = tk.Frame(win_2)
    frame_2.pack()
    txt_2=Label(frame_2,text="Combien de Disk voulez-vous ?")
    txt_2.grid(row=0,column=3,pady=20,padx=100)
    box=Entry(frame_2)        
    box.grid(row=1,column=3)
    btn_valide = tk.Button(frame_2,text="Valider",fg="red")
    btn_valide.grid(row=2,column=3,pady=10,padx=100) 

    try:
        
        def open_disk():
            
            os.system(r"D:\Kraya\2DNI\TP\Eval_Perfor\TP2_evalperform\prog\DiskBench.exe")

        def run_disk():
            
            n=int(float(box.get()))

            for i in range(1,n+1):
        
                _thread.start_new_thread(open_disk)
            win_2.destroy()
    
        btn_valide.config(command=run_disk)
        
        
    except ValueError:
        return "nope"


win = tk.Tk()
win.title("TP2 évaluation de performance")
win.geometry("400x300")
frame = tk.Frame(win)
frame.pack()
btn_cpu = tk.Button(frame,text="DISK BENCH",fg="red",height="5",command=para_window)
btn_cpu.grid(row=0,column=3,pady=10,padx=100)
btn_disk = tk.Button(frame,text="Process Explorer",fg="blue",height="5",width="12",command=run_proc)
btn_disk.grid(row=1,column=3,pady=10,padx=100)

txt=Label(frame,text="© Malek Ghozzi & Med Amine Boufares")
txt.grid(row=3,column=3,pady=50,padx=100)

win.mainloop()