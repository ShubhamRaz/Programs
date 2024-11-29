def pat(a):
    if a<=1:
        return a
    else: return pat(a-1)+pat(a-2)
   

    
print(pat(3))