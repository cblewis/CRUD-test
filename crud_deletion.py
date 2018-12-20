import os

file_path = input("Paste the directory you want to CRUD test here:")
filepath = os.path.join('crudfile_test.txt')
if not os.path.exists(file_path):
    os.makedirs(file_path)
os.chdir(file_path)
os.remove("crudfile_test.txt")
