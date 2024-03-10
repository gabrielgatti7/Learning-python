import os
import shutil

path = "empty_folder"

try:
    os.remove(path)                     # delete a file
    #os.rmdir(path)                      # delete an empty folder
    #shutil.rmtree(path)                 # delete a directory containing files
except FileNotFoundError:
    print(path+ " was not found")
except PermissionError:
    print("Permission denied")
except OSError:
    print("OS error")
else:
    print(path+ " was deleted")