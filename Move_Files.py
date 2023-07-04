import os
import shutil

from_dir = "Image_Files"
to_dir = "Document_Files"

list_of_files = os.listdir(from_dir)


for i in list_of_files:
    root,ext= os.path.splitext(from_dir)
   
print(list_of_files)