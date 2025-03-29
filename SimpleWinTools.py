import tkinter as tk
from tkinter import messagebox, Menu
import subprocess
import pyautogui
import ttkbootstrap as ttk
import threading


def run_command(command):
 def task():
  try:
   output = subprocess.check_output(command, shell=True, text=True)
   messagebox.showinfo("Output", output)
  except subprocess.CalledProcessError:
   messagebox.showerror("Error", "Error")
  except PermissionError:
   messagebox.showerror("Error", "No Admin")
  except Exception:
   messagebox.showerror("Error", "Abort")
 threading.Thread(target=task, daemon=True).start()  

def restart_explorer():
 def task():
  try:
   subprocess.run("taskkill /f /im explorer.exe && start explorer.exe", shell=True)
  except Exception:
   messagebox.showerror("Error", "Abort")
 threading.Thread(target=task, daemon=True).start() 

def show_about():
 messagebox.showinfo("About", "Simple GUI For fixing common windows stuff \nCreated with Tkinter and python (cus its easy to work with) more stuff coming later -stratosvomvos")


root = ttk.Window(themename="darkly") 
root.title("SimpleWindowsTools")
root.geometry("500x410")

menu_bar = Menu(root)
root.config(menu=menu_bar)

about_menu = Menu(menu_bar, tearoff=0) 
about_menu.add_command(label="About", command=show_about)

menu_bar.add_cascade(label="Help", menu=about_menu)


frame = ttk.Frame(root, padding=20)
frame.pack(pady=20)

title_label = tk.Label(root, text="SimpleWindowsTools for 10/11 by stratosvomvos", font=("Arial", 16), pady=11)
title_label.pack()

btn1 = ttk.Button(frame, text="Fix simple GPU driver issues (You should hear a beep and then its done :D)", command=lambda: pyautogui.hotkey('winleft', 'shift', 'ctrl', 'b'))
btn1.pack(pady=5, fill='x')



btn2 = ttk.Button(frame, text="Fix Explorer issues (Desktop will disappear for a second, wait a bit for the taskbar)", command=restart_explorer)
btn2.pack(pady=5, fill='x')


btn3 = ttk.Button(frame, text="Flush DNS and Renew IP (Fix Slow Internet, Or other network Issues)", command=lambda: run_command("ipconfig /flushdns |ipconfig /release & ipconfig /renew "))
btn3.pack(pady=5, fill='x')

btn4 = ttk.Button(frame, text="Scan and repair Windows system files (Will ask for admin)", command=lambda: run_command("powershell Start-Process sfc /scannow -Verb runAs"))
btn4.pack(pady=5, fill='x')

btn5 = ttk.Button(frame, text="Check Disk (Will ask for admin too, will use chkdisk to scan for FileSystem errors", command=lambda: run_command("powershell Start-Process chkdsk -Verb runAs"))
btn5.pack(pady=5, fill='x')


btn6 = ttk.Button(frame, text="Fix more serious windows errors using DISM (will need admin again)", command=lambda: run_command("powershell Start-Process chkdsk -Verb runAs"))
btn6.pack(pady=5, fill='x')


btn7 = ttk.Button(frame, text="ReSync The Date and time (will need admin)", command=lambda: run_command("powershell Start-Process w32tm /resync -Verb runAs"))
btn7.pack(pady=5, fill='x')

btn8 = ttk.Button(frame, text="System Info (Shows all system info in one big box)", command=lambda: run_command("systeminfo"))
btn8.pack(pady=5, fill='x')

root.mainloop()
