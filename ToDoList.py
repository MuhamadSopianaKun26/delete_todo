import msvcrt
import os


def DeleteToDo(x):
    with open('DataToDo.txt', 'r') as file:
        lines = file.readlines()

    with open('DataToDo.txt', 'w') as file:
        for i, line in enumerate(lines):
            ToDo = line.strip().split(',')
            if i != x - 1: 
                file.write(line)

x = int(input("Masukkan angka (ID yang akan dihapus): "))
DeleteToDo(x)

print(f"Data dengan ID {x} telah dihapus.")
