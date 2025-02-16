import os 

with open("modlist.txt") as modlist:
    rootPath = '/mnt/g/Steam/steamapps/common/Baldurs Gate 3/'

    for mod in modlist:
        Path = rootPath.rstrip() + mod.rstrip().replace("\\", "/")
        
        os.remove(Path)
        print(f"removed {Path}")

