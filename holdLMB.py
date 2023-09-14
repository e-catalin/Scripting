import keyboard
import pyautogui

mouse_button_pressed = False

def toggle_mouse_button(e):
    global mouse_button_pressed
    if e.event_type == keyboard.KEY_DOWN and e.name == "a":
        mouse_button_pressed = not mouse_button_pressed
        if mouse_button_pressed:
            print("Pressing LMB")
            pyautogui.mouseDown()
        else:
            print("Releasing LMB")
            pyautogui.mouseUp()

keyboard.hook(toggle_mouse_button)

print("Press 'A' to toggle holding down the left mouse button.")
print("Press 'Esc' to exit.")

keyboard.wait("esc")

# Clean up
keyboard.unhook_all()
pyautogui.mouseUp()
