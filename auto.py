import keyboard
import time
import win32api
import win32con
import customtkinter as ctk
import threading

def click(cps_slider, cps_label):
    cps = round(cps_slider.get())
    delay = 1000 / cps
    try:
        while True:
            if win32api.GetKeyState(win32con.VK_LBUTTON) < 0:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                time.sleep(delay / 1000)  
                while win32api.GetKeyState(win32con.VK_LBUTTON) < 0:
                    cps = cps_slider.get()
                    cps_label.configure(text=f"CPS: {cps}")
                    time.sleep(0.01)  
            if keyboard.is_pressed("G"):  
                break
    except Exception as e:
        print("LeftClick Error:", e)

def start_clicker(cps_slider, cps_label):
    thread = threading.Thread(target=click, args=(cps_slider, cps_label))
    thread.start()

def update_label(cps_slider, cps_label, event=None):
    cps = round(cps_slider.get())
    cps_label.configure(text=f"CPS: {cps}")

def create_ui():
    root = ctk.CTk()
    root.title("AutoClicker")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60)

    label = ctk.CTkLabel(master=frame, text="Enter CPS:")
    label.pack()

    cps_slider = ctk.CTkSlider(master=frame, from_=1, to=20, command=lambda value: update_label(cps_slider, cps_label))
    cps_slider.pack()

    cps_label = ctk.CTkLabel(master=frame, text="CPS: 1")
    cps_label.pack()

    start_button = ctk.CTkButton(master=frame, text="Start", command=lambda: start_clicker(cps_slider, cps_label))
    start_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_ui()