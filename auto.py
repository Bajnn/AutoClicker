import keyboard
import time
import win32api
import win32con
import random
import customtkinter
import threading
def slider_event(value):
    print(value)
    entry3.configure(text=f"Cps Selector {round(value, 3)}")
def leftClick():
    try:
        maxValue = entry2.get()
        while True:
            x = random.uniform(0.15, maxValue)
            time.sleep(x)
            print("Test")
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            if keyboard.is_pressed("G"):
                break
    except:
        print("LeftClick")
def start():
    try:
        while True:
            time.sleep(0.1)
            if keyboard.is_pressed("F"):
                leftClick()    
    except:
        print("Start")

def start_thread():
    global is_running
    if not is_running:
        is_running = True
        thread = threading.Thread(target=start)
        thread.start()

try:
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()
    root.geometry("400x350")
    root.maxsize(400,350)
    root.minsize(400,350)
    root.title("AutoClicker | Bajn")
    

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="AutoClicker | Start (F) | Stop (G)")
    label.pack(pady=12, padx=10, side="top")

    is_running = False  # Variable to track whether the start function is running
    
    entry1 = customtkinter.CTkButton(master=frame, command=start_thread, text="Start/Stop", fg_color="#035afc")
    entry1.pack(pady=12, padx=10, side="bottom")

    entry2 = customtkinter.CTkSlider(master=frame, from_=0.15, to=0.0003, command=slider_event)
    entry2.pack(pady=12, padx=10)
    
    entry3 = customtkinter.CTkLabel(master=frame, text=f"Cps random time values {entry2.get()}")
    entry3.pack(pady=1, padx=1)

    root.mainloop()

except Exception as e:
    print(f"Error: {e}")
