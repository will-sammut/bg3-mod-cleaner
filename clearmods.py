import platform
import shutil
from pathlib import Path

print(f"OS: {platform.system()}")

File = input("Paste the path to the mod list: ")
with open(File) as modlist:
    Result1 = print("Please paste your Baldur's Gate 3 installation path\n  e.g. \n../Steam/steamapps/common/Baldurs Gate 3/")
    installPath = input()

    for mod in modlist:
        ModPath = installPath.rstrip() + mod.rstrip()

        print(f"Found {ModPath}...")
        try:
            path = Path(ModPath)

            Confirmation = input(f"Are you sure you want to delete the following directory and all its contents? (y/n)\n\n{path.parent}/\n")
            if Confirmation == 'y':
                shutil.rmtree(path.parent)
        except FileNotFoundError:
            print(f"removing {ModPath}....NOT FOUND\n")

    print("\n\n....Done! \n\n Remember to verify your game files via Steam to restore any missing files.\n\n") 

