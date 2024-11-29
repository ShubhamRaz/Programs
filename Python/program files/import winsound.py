import winsound

sound={
    "s":1000,
    "r":2000,
    "g":3000,
    "m":4000,
    "p":5000,
    "d":6000,
    "n":7000,
    " ":37

}

music="srgmpdns sndpmgrs"

for note in music:
    winsound.Beep(sound[note],1000)