import tkinter as tk
from random import randint
import time
import threading

root=tk.Tk()

root.title("Testing out Threading stuff")
root.geometry("500x400")

killthread=threading.Event()

def five_seconds():
    my_button1.config(state="disabled")
    kill_button.config(state="normal")
    while True:
        time.sleep(5)
        my_label.config(text="5 seconds done")
        if killthread.is_set():
            my_label.config(text="Thread killed")
            my_button1.config(state="normal")
            break
    

def rando():
    random_label.config(text=f"Random Number {randint(1, 999999)}")

def killthethread():
    killthread.set()


my_label=tk.Label(root, text="This is a label")
my_label.pack(pady=20)

my_button1=tk.Button(root, text="5 seconds", command=lambda: threading.Thread(target=five_seconds).start()) # This will only start the function on click, and any time the button is clicked it should start a new thread (because up there I disable the button unless stuff is killed)
my_button1.pack(pady=20)

my_button2 = tk.Button(root, text="Pick Randm Number", command=rando )
my_button2.pack(pady=20)

random_label=tk.Label(text="")
random_label.pack(pady=20)

kill_button = tk.Button(root, text="Kill this thread", state="disabled", command=killthethread)
kill_button.pack(pady=20)


root.mainloop()