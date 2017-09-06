#Renomear arquivos de uma pasta
import os

def rename_files():

    #(1) Obter os nomes dos arquivos de uma pasta
    file_list = os.listdir(r"/path");
    print(file_list)

    saved_path = os.getcwd()
    print("Pasta atual: " + saved_path)

    os.chdir(r"/path")
   
    #(2) Para cada arquivo, renomear o seu nome
    for file_name in file_list:
      print("Old name: " + file_name)
      os.rename(file_name, file_name.translate(None, "0123456789"))
      print("New name: " + file_name)
    
    os.chdir(saved_path)

rename_files()