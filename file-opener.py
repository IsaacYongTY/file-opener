import tkinter as tk
from tkinter import filedialog, Text
import os, subprocess

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        print(tempApps)
       
        apps = [x for x in tempApps if x.strip()]

def addApp():

    

    filename = filedialog.askopenfilename(initialdir="/Applications", title="Select file", 
                                        filetypes=(("executables", "*.app"),("All Files", "*.*")))

    for widget in frame.winfo_children():
        widget.destroy()
        
    apps.append(filename)
 
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        print(app)
        #for MacOS
        subprocess.call(["open", app])

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runFile = tk.Button(root, text="Run File", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runFile.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop() 

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')