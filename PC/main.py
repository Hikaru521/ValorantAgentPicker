import mouse
import keyboard
import time
import agents
import gui
import threading

def teleport(x, y):
    mouse.move(x, y)
    #mouse.click()
    time.sleep(0.01)

keyboard_cooldown = 0
is_running = False

def loop():
    global is_running
    global keyboard_cooldown
    while True:
        if is_running:
            teleport(agents.selected_agent[0], agents.selected_agent[1])
            teleport(960, 725)
            #print("teleported")
        if keyboard_cooldown <= time.time_ns() and keyboard.is_pressed('space'):
            keyboard_cooldown = time.time_ns() + 250000000
            #print("Not teleported")
            is_running = not is_running

thread = threading.Thread(target=loop)
thread.start()
gui.open_gui(thread)