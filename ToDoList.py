import msvcrt
import os

data = [
{"id":1, "todo":"Makan", "jam":"10.00"}

]

def DeleteToDo(x):
    with open('Data.txt', 'r') as file:
        lines = file.readlines()

    with open('Data.txt', 'w') as file:
        for i, line in enumerate(lines):
            line.strip().split(',')
            if i != x - 1: 
                file.write(line)

def Readfile():
    Data = {}
    path = "Data.txt"
    cek_file = os.path.isfile(path)
    
    if not cek_file:
        with open(path, 'w') as file:
            file.write("")
    else:
        with open(path, 'r') as file:

            for line in file:
                Isi = line.strip().split(",")
                if len(Isi) == 3:
                    key, do, jam = Isi
                    Data[key] = {"Do": do, "Jam": jam}

            file.close()

            for key, value in Data.items():
                print(f"{key}. Do: {value['Do']}, Jam: {value['Jam']}")
    

Readfile()
DeleteToDo(4)