# import module 
import os 


# list files
all_files = os.listdir(".")

for file in all_files:

    # key or message file : remove it
    if "pem" in file or "message" in file:
        print("(*) Removing : ", file)
        os.remove(file)
