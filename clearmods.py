import os 
import tkinter as tk
import platform
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

# Show the message box

Result0 = messagebox.showinfo("BG3 Mod Cleaner", "Please open the modlist file.")
if Result0 == 'ok':
    File = tk.filedialog.askopenfile()
    with open(File.name) as modlist:
        with open("clearmods_log.txt", "w") as log:
            Result1 = messagebox.showinfo("BG3 Mod Cleaner", "Please select your Baldur's Gate 3 installation path\n  e.g. \nSteam/steamapps/common/Baldurs Gate 3/")
            if Result1 == 'ok':
                installPath = tk.filedialog.askdirectory()

                for mod in modlist:
                    if platform.system() == 'Windows':
                        ModPath = installPath.rstrip() + mod.rstrip().replace("\\", "/")
                    else:
                        ModPath = installPath.rstrip() + mod.rstrip()

                    try:
                        os.remove(ModPath)
                        log.write(f"removing {ModPath}....OK\n")
                    except FileNotFoundError:
                        log.write(f"removing {ModPath}....NOT FOUND\n")

                messagebox.showinfo("BG3 Mod Cleaner", "Done.")

# Run the Tkinter event loop
root.mainloop()
