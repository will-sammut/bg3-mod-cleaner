import os 
import platform
from pathlib import Path
import shutil

print(f"OS: {platform.system()}")

File = input("Paste the path to the mod list: ")
with open(File) as modlist:
    Result1 = print("Please paste your Baldur's Gate 3 installation path\n  e.g. \n../Steam/steamapps/common/Baldurs Gate 3/")
    installPath = input()

    for mod in modlist:
        ModPath = installPath.rstrip() + mod.rstrip()

        print(ModPath)
        try:
            path = Path(ModPath)
            print(f"removing {path.parent}...OK")
            shutil.rmtree(path.parent)
        except FileNotFoundError:
            print(f"removing {ModPath}....NOT FOUND\n")

        print("\n\n....DONE")

