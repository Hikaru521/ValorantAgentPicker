from tkinter import *
import agents

def pick_neon():
    agents.selected_agent = agents.agents["Neon"]
    print("Picked: Neon")

def pick_jett():
    agents.selected_agent = agents.agents["Jett"]
    print("Picked: Jett")

def pick_clove():
    agents.selected_agent = agents.agents["Clove"]
    print("Picked: Clove")
th = None
def gui_exit():
    global th
    exit("Szelya!")
def open_gui(thread):
    global th
    window.eval('tk::PlaceWindow . center')
    th = thread
    window.mainloop()

window = Tk()
window.title("Agent Picker")

gomb_clove = Button(window, text='Clove')
gomb_clove.config(command=pick_clove)
kep_clove = PhotoImage(file="Clove.png")
gomb_clove.config(image=kep_clove)
gomb_clove.grid(row=0, column=1, padx=10, pady=10)

gomb_clove = Button(window, text='Neon')
gomb_clove.config(command=pick_neon)
kep_neon = PhotoImage(file="Neon.png")
gomb_clove.config(image=kep_neon)
gomb_clove.grid(row=0, column=0, padx=10, pady=10)

gomb_clove = Button(window, text='Jett')
gomb_clove.config(command=pick_jett)
kep_jett = PhotoImage(file="Jett.png")
gomb_clove.config(image=kep_jett)
gomb_clove.grid(row=0, column=2, padx=10, pady=10)

window.resizable(False, False)
