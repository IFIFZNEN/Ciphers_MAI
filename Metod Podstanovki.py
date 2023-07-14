code_list_shifrovanie = [("A", "Z"), ("B", "Y"), ("C", "X"), ("D", "W"), ("E", "V"), ("F", "U"),
             ("G", "T"), ("H", "S"), ("I", "R"), ("J", "Q"), ("K", "P"), ("L", "O"),
             ("M", "N"), ("N", "M"), ("O", "L"), ("P", "K"), ("Q", "J"), ("R", "I"),
             ("S", "H"), ("T", "G"), ("U", "F"), ("V", "E"), ("W", "D"), ("X", "C"),
             ("Y", "B"), ("Z", "A"), (" ", "?"), (".", " "), (",", "!"), ("!", "#"),
             (":", "@"), (";", "%"), ("?", "{"), ("-", "^"),("_", "}")]
 
code_list_deshifrovanie = [("Z", "A"), ("Y", "B"), ("X", "C"), ("W", "D"), ("V", "E"), ("U", "F"),
             ("T", "G"), ("S", "H"), ("R", "I"), ("Q", "J"), ("P", "K"), ("O", "L"),
             ("N", "M"), ("M", "N"), ("L", "O"), ("K", "P"), ("J", "Q"), ("I", "R"),
             ("H", "S"), ("G", "T"), ("F", "U"), ("E", "V"), ("D", "W"), ("C", "X"),
             ("B", "Y"), ("A", "Z"), ("?", " "), (" ", "."), ("!", ","), ("#", "!"),
             ("@", ":"), ("%", ";"), ("{", "?"), ("^", "-"),("}", "_")]


print("/////////////////////////////METOD PROSTOY PODSTANOVKI/////////////////////\n/////////////////////////////VIBERITE FUNKCIYU/////////////////////////////")
vibor = int(input("/////////////////////////////SHIFROVANIE (1)/////////////////////////////\n////////////////////////////////DESIFROVANIE (2)/////////////////////////////\n/////////////////////////////VASH VIBOR:"))

if vibor == 1:
    data = input("Vvedite text dlya shifrovaniya: ")
    print(data.upper().translate(str.maketrans(dict(code_list_shifrovanie))))

elif vibor == 2:
    data = input("Vvedite text dlya deshifrovaniya: ")
    print(data.upper().translate(str.maketrans(dict(code_list_deshifrovanie))))

