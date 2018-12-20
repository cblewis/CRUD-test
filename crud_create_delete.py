#!/usr/bin/env python3

import os
import time

#Masterfully crafted by Cameron Lewis
file_path = input("Paste the directory you want to CRUD test here:")
print("This will close automatically once its sorcery is complete.")
filepath = os.path.join('crudfile_test.txt')
if not os.path.exists(file_path):
    os.makedirs(file_path)
os.startfile(file_path)
os.chdir(file_path)
with open("crudfile_test.txt", 'w') as file:
    file.write("This file has been made to automate")
    file.write("\nCRUD testing these directories.")
    #file.close()
time.sleep(5.0)
os.remove("crudfile_test.txt")