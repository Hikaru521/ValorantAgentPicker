from tkinter import *
import agents

def pick_astra():
    agents.selected_agent = agents.agents["Astra"]
    print("Picked: Astra")

def pick_breach():
    agents.selected_agent = agents.agents["Breach"]
    print("Picked: Breach")

def pick_brimstone():
    agents.selected_agent = agents.agents["Brimstone"]
    print("Picked: Brimstone")

def pick_chamber():
    agents.selected_agent = agents.agents["Chamber"]
    print("Picked: Chamber")

def pick_clove():
    agents.selected_agent = agents.agents["Clove"]
    print("Picked: Clove")

def pick_cypher():
    agents.selected_agent = agents.agents["Cypher"]
    print("Picked: Cypher")

def pick_deadlock():
    agents.selected_agent = agents.agents["Deadlock"]
    print("Picked: Deadlock")

def pick_fade():
    agents.selected_agent = agents.agents["Fade"]
    print("Picked: Fade")

def pick_gekko():
    agents.selected_agent = agents.agents["Gekko"]
    print("Picked: Gekko")

def pick_harbor():
    agents.selected_agent = agents.agents["Harbor"]
    print("Picked: Harbor")

def pick_iso():
    agents.selected_agent = agents.agents["Iso"]
    print("Picked: Iso")

def pick_jett():
    agents.selected_agent = agents.agents["Jett"]
    print("Picked: Jett")

def pick_kayo():
    agents.selected_agent = agents.agents["Kay/o"]
    print("Picked: Kay/o")

def pick_killjoy():
    agents.selected_agent = agents.agents["Killjoy"]
    print("Picked: Killjoy")

def pick_neon():
    agents.selected_agent = agents.agents["Neon"]
    print("Picked: Neon")

def pick_omen():
    agents.selected_agent = agents.agents["Omen"]
    print("Picked: Omen")

def pick_phoenix():
    agents.selected_agent = agents.agents["Phoenix"]
    print("Picked: Phoenix")

def pick_raze():
    agents.selected_agent = agents.agents["Raze"]
    print("Picked: Raze")

def pick_reyna():
    agents.selected_agent = agents.agents["Reyna"]
    print("Picked: Reyna")

def pick_sage():
    agents.selected_agent = agents.agents["Sage"]
    print("Picked: Sage")

def pick_skye():
    agents.selected_agent = agents.agents["Skye"]
    print("Picked: Skye")

def pick_sova():
    agents.selected_agent = agents.agents["Sova"]
    print("Picked: Sova")

def pick_viper():
    agents.selected_agent = agents.agents["Viper"]
    print("Picked: Viper")

def pick_vyse():
    agents.selected_agent = agents.agents["Vyse"]
    print("Picked: Vyse")

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

gomb_astra = Button(window, text='Astra')
gomb_astra.config(command=pick_astra)
kep_astra = PhotoImage(file="Astra.png")
gomb_astra.config(image=kep_astra)
gomb_astra.grid(row=0, column=0, padx=10, pady=10)

gomb_breach = Button(window, text='Breach')
gomb_breach.config(command=pick_breach)
kep_breach = PhotoImage(file="Breach.png")
gomb_breach.config(image=kep_breach)
gomb_breach.grid(row=0, column=1, padx=10, pady=10)

gomb_brimstone = Button(window, text='Brimstone')
gomb_brimstone.config(command=pick_brimstone)
kep_brimstone = PhotoImage(file="Brimstone.png")
gomb_brimstone.config(image=kep_brimstone)
gomb_brimstone.grid(row=0, column=2, padx=10, pady=10)

gomb_chamber = Button(window, text='Chamber')
gomb_chamber.config(command=pick_chamber)
kep_chamber = PhotoImage(file="Chamber.png")
gomb_chamber.config(image=kep_chamber)
gomb_chamber.grid(row=0, column=3, padx=10, pady=10)

gomb_clove = Button(window, text='Clove')
gomb_clove.config(command=pick_clove)
kep_clove = PhotoImage(file="Clove.png")
gomb_clove.config(image=kep_clove)
gomb_clove.grid(row=1, column=0, padx=10, pady=10)

gomb_cypher = Button(window, text='Cypher')
gomb_cypher.config(command=pick_cypher)
kep_cypher = PhotoImage(file="Cypher.png")
gomb_cypher.config(image=kep_cypher)
gomb_cypher.grid(row=1, column=1, padx=10, pady=10)

gomb_deadlock = Button(window, text='Deadlock')
gomb_deadlock.config(command=pick_deadlock)
kep_deadlock = PhotoImage(file="Deadlock.png")
gomb_deadlock.config(image=kep_deadlock)
gomb_deadlock.grid(row=1, column=2, padx=10, pady=10)

gomb_fade = Button(window, text='Fade')
gomb_fade.config(command=pick_fade)
kep_fade = PhotoImage(file="Fade.png")
gomb_fade.config(image=kep_fade)
gomb_fade.grid(row=1, column=3, padx=10, pady=10)

gomb_gekko = Button(window, text='Gekko')
gomb_gekko.config(command=pick_gekko)
kep_gekko = PhotoImage(file="Gekko.png")
gomb_gekko.config(image=kep_gekko)
gomb_gekko.grid(row=2, column=0, padx=10, pady=10)

gomb_harbor = Button(window, text='Harbor')
gomb_harbor.config(command=pick_harbor)
kep_harbor = PhotoImage(file="Harbor.png")
gomb_harbor.config(image=kep_harbor)
gomb_harbor.grid(row=2, column=1, padx=10, pady=10)

gomb_iso = Button(window, text='Iso')
gomb_iso.config(command=pick_iso)
kep_iso = PhotoImage(file="Iso.png")
gomb_iso.config(image=kep_iso)
gomb_iso.grid(row=2, column=2, padx=10, pady=10)

gomb_jett = Button(window, text='Jett')
gomb_jett.config(command=pick_jett)
kep_jett = PhotoImage(file="Jett.png")
gomb_jett.config(image=kep_jett)
gomb_jett.grid(row=2, column=3, padx=10, pady=10)

gomb_kayo = Button(window, text='Kay/o')
gomb_kayo.config(command=pick_kayo)
kep_kayo = PhotoImage(file="Kayo.png")
gomb_kayo.config(image=kep_kayo)
gomb_kayo.grid(row=3, column=0, padx=10, pady=10)

gomb_killjoy = Button(window, text='Killjoy')
gomb_killjoy.config(command=pick_killjoy)
kep_killjoy = PhotoImage(file="Killjoy.png")
gomb_killjoy.config(image=kep_killjoy)
gomb_killjoy.grid(row=3, column=1, padx=10, pady=10)

gomb_neon = Button(window, text='Neon')
gomb_neon.config(command=pick_neon)
kep_neon = PhotoImage(file="Neon.png")
gomb_neon.config(image=kep_neon)
gomb_neon.grid(row=3, column=2, padx=10, pady=10)

gomb_omen = Button(window, text='Omen')
gomb_omen.config(command=pick_omen)
kep_omen = PhotoImage(file="Omen.png")
gomb_omen.config(image=kep_omen)
gomb_omen.grid(row=3, column=3, padx=10, pady=10)

gomb_phoenix = Button(window, text='Phoenix')
gomb_phoenix.config(command=pick_phoenix)
kep_phoenix = PhotoImage(file="Phoenix.png")
gomb_phoenix.config(image=kep_phoenix)
gomb_phoenix.grid(row=4, column=0, padx=10, pady=10)

gomb_raze = Button(window, text='Raze')
gomb_raze.config(command=pick_raze)
kep_raze = PhotoImage(file="Raze.png")
gomb_raze.config(image=kep_raze)
gomb_raze.grid(row=4, column=1, padx=10, pady=10)

gomb_reyna = Button(window, text='Reyna')
gomb_reyna.config(command=pick_reyna)
kep_reyna = PhotoImage(file="Reyna.png")
gomb_reyna.config(image=kep_reyna)
gomb_reyna.grid(row=4, column=2, padx=10, pady=10)

gomb_sage = Button(window, text='Sage')
gomb_sage.config(command=pick_sage)
kep_sage = PhotoImage(file="Sage.png")
gomb_sage.config(image=kep_sage)
gomb_sage.grid(row=4, column=3, padx=10, pady=10)

gomb_skye = Button(window, text='Skye')
gomb_skye.config(command=pick_skye)
kep_skye = PhotoImage(file="Skye.png")
gomb_skye.config(image=kep_skye)
gomb_skye.grid(row=5, column=0, padx=10, pady=10)

gomb_sova = Button(window, text='Sova')
gomb_sova.config(command=pick_sova)
kep_sova = PhotoImage(file="Sova.png")
gomb_sova.config(image=kep_sova)
gomb_sova.grid(row=5, column=1, padx=10, pady=10)

gomb_viper = Button(window, text='Viper')
gomb_viper.config(command=pick_viper)
kep_viper = PhotoImage(file="Viper.png")
gomb_viper.config(image=kep_viper)
gomb_viper.grid(row=5, column=2, padx=10, pady=10)

gomb_vyse = Button(window, text='Vyse')
gomb_vyse.config(command=pick_vyse)
kep_vyse = PhotoImage(file="Vyse.png")
gomb_vyse.config(image=kep_vyse)
gomb_vyse.grid(row=5, column=3, padx=10, pady=10)

window.resizable(False, False)