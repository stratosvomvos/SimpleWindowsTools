import tkinter as tk
from tkinter import messagebox, Menu
from tkinter import ttk
import subprocess
import pyautogui
import threading
import ttkbootstrap as ttk

# function to run shell commands (thank chatgpt for this one)
def run_command(command):
    def execute():
        try:
            output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
            messagebox.showinfo("Info", output)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error!!", f"Failed!")
        except PermissionError:
            messagebox.showerror("Error", "Failed")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error:")

    thread = threading.Thread(target=execute, daemon=True)
    thread.start()

# seperate function to restart explorer cus it was breaking tkinter before
def restart_explorer():
    def execute():
        try:
            subprocess.run("taskkill /f /im explorer.exe && start explorer.exe", shell=True, check=True)
        except subprocess.SubprocessError:
            messagebox.showerror("Error", "Failed to restart Windows Explorer.")

    threading.Thread(target=execute, daemon=True).start()
def show_about():
 messagebox.showinfo("About", "A Simple GUI For common windows stuff \nCreated with Tkinter and python (cus its easy to work with) more stuff coming later -stratosvomvos")

# initialize window (tkinter stuff)
root = ttk.Window(themename="darkly")
root.title("SimpleWindowsTools (V0.2)")
root.geometry("550x350")



# menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Main", menu=help_menu)

# title

title_label = tk.Label(root, text="SimpleWindowsTools for Windows 10/11", font=("Arial", 14), pady=10)
title_label.pack()

title_label = tk.Label(root, text="by stratosvomvos", font=("Arial", 14), pady=10)

title_label.pack()

# tabs (just learned about tkinter tabs so you will see them in other projects now)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

#Gpu tab
system_tab = ttk.Frame(notebook)
notebook.add(system_tab, text='Graphics mostly')


ttk.Button(system_tab, text="Fix Explorer issues (Desktop will disappear for a second, wait a bit for the taskbar)", command=restart_explorer).pack(pady=5, fill='x')

ttk.Button(system_tab, text="Fix simple GPU driver issues (You should hear a beep and then its done :D)", command=lambda: pyautogui.hotkey('winleft', 'shift', 'ctrl', 'b')).pack(pady=5, fill='x')

ttk.Button(system_tab, text="Run DXDIAG (run the DirectX diagnostics tool)", command=lambda: run_command("dxdiag")).pack(pady=5, fill='x')



# Network related
network_tab = ttk.Frame(notebook)
notebook.add(network_tab, text='Network stuff')
ttk.Button(network_tab, text="Flush DNS & Renew IP (will take abt 30 secs)", command=lambda: run_command("powershell ipconfig /flushdns && ipconfig /renew")).pack(pady=5, fill='x')
ttk.Button(network_tab, text="ReSync The Date and time (will need admin)", command=lambda: run_command("powershell Start-Process w32tm /resync -Verb runAs")).pack(pady=5, fill='x')
ttk.Button(network_tab, text="Ping Google.com (pings google)", command=lambda: run_command("ping google.com")).pack(pady=5, fill='x')
ttk.Button(network_tab, text="Whats my mac address?", command=lambda: run_command("getmac")).pack(pady=5, fill='x')

#Performance and optimizations
performance_tab = ttk.Frame(notebook)
notebook.add(performance_tab, text='General Optimizations')
ttk.Button(performance_tab, text="Defrag C: drive (will help if you still have a boot HDD for some reason)", command=lambda: run_command("powershell Start-Process defrag C: -Verb runAs")).pack(pady=5, fill='x')
ttk.Button(performance_tab, text="Scan and repair Windows system files (Will ask for admin)", command=lambda: run_command("powershell Start-Process sfc /scannow -Verb runAs")).pack(pady=5, fill='x')
ttk.Button(performance_tab, text="Check Disk (Will ask for admin too, will use chkdisk to scan for FileSystem errors", command=lambda: run_command("powershell Start-Process chkdsk -Verb runAs")).pack(pady=5, fill='x')

# Miscellaneous 
misc_tab = ttk.Frame(notebook)
notebook.add(misc_tab, text='Misc')
ttk.Button(misc_tab, text="Reboot to bios", command=lambda: run_command("shutdown.exe /r /fw")).pack(pady=5, fill='x')
ttk.Button(misc_tab, text="Shutdown the pc", command=lambda: run_command("shutdown /s /t 0")).pack(pady=5, fill='x')
ttk.Button(misc_tab, text="Open the Task Manager", command=lambda: run_command("taskmgr")).pack(pady=5, fill='x')
ttk.Button(misc_tab, text="Open Device Manager (pretty self explanatory)", command=lambda: run_command("devmgmt.msc")).pack(pady=5, fill='x')
ttk.Button(misc_tab, text="System Info (Shows all system info in one big box)", command=lambda: run_command("systeminfo")).pack(pady=5, fill='x')


root.mainloop()
