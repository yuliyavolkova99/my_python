atom_number = input("Ведите номер химического элемента: ")
if atom_number:
    элемент = int(atom_number)
    if элемент == 3:
        print("Li")
    elif элемент == 25:
        print("Mn")
    elif элемент == 80:
        print("Hg")
    elif элемент == 17:
        print("Cl")
    else:
        print("Химический элемент не определен!")
else:
    print("Ведите номер химического элемента: ")
