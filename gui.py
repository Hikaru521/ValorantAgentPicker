from tkinter import *
import agents

def pick_reyna():
    agents.selected_agent = agents.agents["Reyna"]
    print("picked: Reyna")

def pick_clove():
    agents.selected_agent = agents.agents["Clove"]
    print("picked: Clove")
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

window.resizable(False, False)
