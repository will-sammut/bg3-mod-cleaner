import os 
import platform

print(f"OS: {platform.system()}")

File = input("Paste the path to the mod list: ")
with open(File) as modlist:
    Result1 = print("BG3 Mod Cleaner \n\nPlease paste your Baldur's Gate 3 installation path\n  e.g. \n../Steam/steamapps/common/Baldurs Gate 3/")
    installPath = input()

    print(f"Removing leftover files from {installPath}")

    for mod in modlist:
        ModPath = installPath.rstrip() + mod.rstrip()

        print(ModPath)
        try:
            os.remove(ModPath)
            print(f"removing {ModPath}....OK\n")
        except FileNotFoundError:
            print(f"removing {ModPath}....NOT FOUND\n")

        print("\n\n....DONE")

