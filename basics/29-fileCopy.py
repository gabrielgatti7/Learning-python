# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file's creation and modification times)
import shutil

# args = src,dest
shutil.copyfile("C:\\Users\\gabri\\Desktop\\test.txt", "C:\\Users\\gabri\\Desktop\\copy.txt")