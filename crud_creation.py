import os

file_path = input("Paste the directory you want to CRUD test here:")
if not os.path.exists(file_path):
    os.makedirs(file_path)
    filepath = os.path.join(file_path + 'crudfile_test.txt')
os.chdir(file_path)
crudfile = open("crudfile_test.txt", "w")
crudfile.write("This file has been made to automate")
crudfile.write("\nCRUD testing these directories.")
crudfile.close()
