dict={
    "a":"!",
    "b":"Z",
    "c":"m",
    "d":"S",
    "e":"d",
    "f":"y",
    "g":"P",
    "h":"l",
    "i":"M",
    "j":"B",
    "k":"0",
    "l":"9",
    "m":"8",
    "n":"7",
    "o":"5",
    "p":"4",
    "q":"3",
    "r":"2",
    "s":"1",
    "t":"(",
    "u":"*",
    "v":")",
    "w":"^",
    "x":"%",
    "y":"$",
    "z":"#",
    " ":"/"
}

rev={
    "!":"a",
    "Z":"b",
    "m":"c",
    "S":"d",
    "d":"e",
    "y":"f",
    "p":"g",
    "l":"h",
    "M":"i",
    "B":"j",
    "0":"k",
    "9":"l",
    "8":"m",
    "7":"n",
    "5":"o",
    "4":"p",
    "3":"q",
    "2":"r",
    "1":"s",
    "(":"t",
    "*":"u",
    ")":"v",
    "^":"w",
    "%":"x",
    "$":"y",
    "#":"z",
    "/":" "
}

print("Type: code or decode")
flag=input("Enter type: ")

if flag=="Code" or flag=="code":
    print("You can right your secret code:-\n")
    newcode=str(input("Enter your line: "))
    for newline in newcode:
        print(dict[newline],end="")

elif flag=="Decode" or flag=="decode":
    print("From here you can decode your secret code:-\n")
    reverse_code=str(input("Enter your secret code"))
    for old_line in reverse_code:
        print(rev[old_line],end="")   



