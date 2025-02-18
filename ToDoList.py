import msvcrt
import os

#Function untuk menghapus list pada file dengan indeks yang ditentukan
def DeleteTodo(x):
    with open('Data.txt', 'r') as file:
        lines = file.readlines()

    with open('Data.txt', 'w') as file:
        for i, line in enumerate(lines):
            line.strip().split(',')
            if i != x - 1: 
                file.write(line)

#Function untuk membaca file dan memprint semua isinya
def ReadFile():
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

# Function untuk mengembalikan array yang berisi ID-ID yang sudah terpakai pada file
def List_IDused():
    ID_used = set()
    try:
        with open("Data.txt", "r") as file:
            for line in file:
                data = line.strip().split(",") 
                if data: 
                    ID_used.add(data[0])  
    except FileNotFoundError:
        print("File tidak ditemukan, membuat file baru...")
    
    return ID_used

# Function untuk menambahkan isi To Do List dan memasukannya kedalam file
def AddTodo():

    ID_used = List_IDused()
    end = False
    file = open("Data.txt", "a")

    while (not end):

        while True:
            id = str(input("\nMasukkan Id: "))
            if id in ID_used:
                print("ID ",id," sudah digunakan, silahkan masukan ID lain!")
            else : 
                break

        todo = str(input("Masukkan kegiatan: "))
        jam = str(input("Masukkan jam: "))

        file.write(id + ",")
        file.write(todo + ",")
        file.write(jam )
        file.write("\n")

        out = input("Tambah lagi? Ketik 1 jika ya: ")
        end = True

        if out == 1:
            end = False
        elif out == "" or out != 1:
            break

    file.close()


AddTodo()
ReadFile()
