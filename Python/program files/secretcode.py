print("Please follow the correct instructions")

dict = {
        "a": "!", "A": "/",
        "b": "&", "B": "|",
        "c": "m", "C": ".",
        "d": "+", "D": ",",
        "e": "d", "E": ">",
        "f": "y", "F": "'",
        "g": "P", "G": ";",
        "h": "l", "H": ":",
        "i": "=", "I": "A",
        "j": "6", "J": "B",
        "k": "0", "K": "C",
        "l": "9", "L": "S",
        "m": "8", "M": "F",
        "n": "7", "N": "G",
        "o": "5", "O": "Q",
        "p": "4", "P": "W",
        "q": "3", "Q": "E",
        "r": "2", "R": "D",
        "s": "1", "S": "T",
        "t": "(", "T": "Y",
        "u": "*", "U": "I",
        "v": ")", "V": "O",
        "w": "^", "W": "t",
        "x": "%", "X": "s",
        "y": "$", "Y": "i",
        "z": "#", "Z": "x",
        " ": "<", ".": "o",
        "1": "_", "6": "L",
        "2": "H", "7": "M",
        "3": "J", "8": "N",
        "4": "-", "9": "R",
        "5": "K", "0": "U",
        ",": "V"
    }

key_list=list(dict.keys())
value_list=list(dict.values())

start=str(input("Enter Y to continue: "))

while start=="y" or start=="Y":

    
    print("Type= code or decode")
    flag = input("Enter Type: ")

    

    if flag == "Code" or flag == "code":
        print("Enter Line to convert and it must be Alphabets:-")
        newcode = str(input("Enter your line: "))

        print("Secret Code:- ",end="")

        for newline in newcode:

            print(dict[newline], end="")
        print()


    elif flag == "Decode" or flag == "decode":
        print("From here you can Decode your secret code:-")

        line=str(input("Enter Secret code: "))
        print('Decoded: ',end="")

        for newline in line:
            reverse_code = value_list.index(newline)      #position of values
            print(key_list[reverse_code],end="")
        print()
        

    else:
        print("Invalid Type, It must be 'code' or 'decode'")
        

    start=str(input("Enter Y to continue: "))

#made by pankaj

