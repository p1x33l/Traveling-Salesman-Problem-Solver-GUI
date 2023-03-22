from pathlib import Path
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import pandas as pd
import numpy as np 
from algo_2opt import *
from algo_pd import *
from graph_draw import *
import time




def calcul(sym,meth,sheet):
    g=pd.read_excel(xls, sheet)
    g=g.drop(['Unnamed: 0'], axis=1)
    if(sym==True):
        g = np.triu(g) + np.triu(g,1).T
    else:
        g=np.array(g)


    if(meth==1):
        start_time = time.time()
        r=dynamique(g)
        end_time = time.time()
        chemin=r[1]
        cout=r[0]
    
    if(meth==2):
        start_time = time.time()
        r=deux_opt(g)
        end_time=time.time()
        chemin=r
        cout=cost(g,r)
    
    duree=end_time - start_time

    graph=[(chemin[i],chemin[i+1]) for i in range(len(chemin)-1)]+[(chemin[-1],chemin[0])]
    labels = [g[i][j] for i,j in graph]
    draw_graph(cout,chemin,graph,duree,labels)


def UploadAction(event=None):
    global xls
    filename = filedialog.askopenfilename()
    xls = pd.ExcelFile(filename)



    
window = Tk()

window.geometry("485x340")
window.configure(bg = "#F4F6FF")

window.title('Probleme du Voyageur de Commerce')

canvas = Canvas(
    window,
    bg = "#F4F6FF",
    height = 340,
    width = 485,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    46.0,
    134.0,
    anchor="nw",
    text="Importez les données (.xlsx):",
    fill="#000000",
    font=("sans-serif", 12 * -1)
)

canvas.create_text(
    46.0,
    162.0,
    anchor="nw",
    text="Nom d’instance :",
    fill="#000000",
    font=("sans-serif", 12 * -1),
)

canvas.create_text(
    46.0,
    216.0,
    anchor="nw",
    text="Algorithme :",
    fill="#000000",
    font=("sans-serif", 12 * -1)
)

button_1 = Button(
    borderwidth=0,
    highlightthickness=0,
    command=lambda: calcul(radio1.get(),radio2.get(),entry_1.get()),
    relief="flat",
    bg='#0984e3',
    fg='white',
    text ="Commencer"
)
button_1.place(
    x=145.0,
    y=285.0,
    width=194.3000030517578,
    height=29.0
)

canvas.create_text(
    46.0,
    191.0,
    anchor="nw",
    text="Données symétrique?",
    fill="#000000",
    font=("sans-serif", 12 * -1)
)


s = ttk.Style()
s.configure('Wild.TRadiobutton',
    background="#F4F6FF",
    foreground='black'
)

radio1 = IntVar()  
ttk.Radiobutton(
    window, 
    text="Oui", 
    variable=radio1, 
    value=True,
    style = 'Wild.TRadiobutton'
).place(
    x=257.0,
    y=191.0
)
  
ttk.Radiobutton(
    window, 
    text="Non", 
    variable=radio1, 
    value=False, 
    style = 'Wild.TRadiobutton'
).place(
    x=314.0,
    y=191.0,
)
 
radio2 = IntVar()  

ttk.Radiobutton(
    window, 
    text="Programmation Dynamique", 
    variable=radio2, 
    value=1,
    style = 'Wild.TRadiobutton'
).place(
    x=257.0,
    y=216.0
)
  
ttk.Radiobutton(
    window, 
    text="Heuristique : 2-OPT", 
    variable=radio2, 
    value=2, 
    style = 'Wild.TRadiobutton'
).place(
    x=257.0,
    y=240.0,
)
 
canvas.create_text(
    100.0,
    25.0,
    anchor="nw",
    text="Probleme du Voyageur de",
    fill="#273C75",
    font=("sans-serif Bold", 24 * -1)
)

canvas.create_text(
    180.0,
    55.0,
    anchor="nw",
    text="Commerce",
    fill="#273C75",
    font=("sans-serif Bold", 24 * -1)
)

entry_bg_1 = canvas.create_image(
    354.0,
    169.5,
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=263.0,
    y=160.0,
    width=182.0,
    height=17.0
)

entry_bg_2 = canvas.create_image(
    353.0,
    141.5,
)
entry_2 = Button(window, 
    text='Choisir un fichier', 
    command=UploadAction,
    bg='#fff',
    borderwidth = '0'
    )
entry_2.place(
    x=262.0,
    y=132.0,
    width=182.0,
    height=17.0
)

canvas.create_rectangle(
    95.0,
    104.0,
    388.0,
    105.0,
    fill="#000000",
    outline="")

canvas.create_text(
    6.0,
    325.0,
    anchor="nw",
    text="BY MOHAMED ELAZZAOUI, YASSINE AFRACHE & BOUKOUTAYA OUSSAMA",
    fill="#000000",
    font=("sans-serif", 10 * -1)
)



window.resizable(False, False)
window.mainloop()
