import os 

with open("modlist.txt") as modlist:

    # Replace with the path to your BG3 installation.
    # e.g. /mnt/g/Steam/steamapps/common/Baldurs Gate 3/

    installPath = ''

    for mod in modlist:
        ModPath = installPath.rstrip() + mod.rstrip().replace("\\", "/")
        
        os.remove(ModPath)
        print(f"removed {ModPath}")

