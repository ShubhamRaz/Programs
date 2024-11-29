import winsound

dict={
    "a":100,
    "b":200,
    "c":300
}

new="acbcab"

for i in new:
    winsound.Beep(dict[i],1000)




