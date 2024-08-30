import mouse

def on_click(event):
    if isinstance(event, mouse.ButtonEvent):
        if event.event_type == 'down' and event.button == 'left':
            x, y = mouse.get_position()
            print(f"Bal kattintás helye: x={x}, y={y}")

mouse.hook(on_click)

try:
    mouse.wait()
except KeyboardInterrupt:
    mouse.unhook(on_click)
    print("Program leállítva.")