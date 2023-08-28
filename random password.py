try:
    from string import ascii_letters, digits, punctuation, join
except ImportError:
    from string import ascii_letters, digits, punctuation
from random import choice, sample, randint

def isEven(integer):
    return integer % 2 == 0

def RandPass(size = 8):
    s0 = "!@#$%^&*- _~+-="
    s1 = ascii_letters
    s3 = digits
    
    s = s0 + s1
    s_full = s + s3
    # passlen = size
    new_password = ""

    # assigning specific sizes for each section of the pw generated
    if isEven(size) == True:
        front = size // 5
    else:
        front = size // 2
    mid = 2
    previous = size - (front + mid) - 1

    pass0 = "".join(choice(s0)) # forces a minimum number of punctuations in the middle
    pass1 = "".join(sample(s_full,front ))
    pass2 = "".join(sample(s3,mid))
    # NO punctuations as 1st character!!! 
    pass3 = "".join(sample(s, previous ))
    # sometimes integer division reduces the size of the desired password length, the following adjusts it back
    if size != len(pass0 + pass1 + pass2 + pass3):
        pass2 = "".join(sample(s3,size - (front+previous+1) ))

    if pass3[:-1] == ' ': # to avoid having an empty space at the end of password
        temp = list(pass3)
        temp[:-1] = choice(s)
        pass3 = ''.join(str(e) for e in temp)
    new_password = pass0 + pass1 + pass2 + pass3    
    
    if size <= 8:
        msg = 'VERY WEAK'
        colorVal = "#6d0001"
    elif size <=10:
        msg = 'WEAK'
        colorVal = "#cc0000"
    elif size <=12:
        msg = 'DECENT'
        colorVal = "#fc8600"
    elif size <=14:
        msg = 'GOOD'
        colorVal = "#eae200"
    elif size <=16:
        msg = 'STRONG'
        colorVal = "#9ff400"
    elif size <=18:
        msg = 'VERY STRONG'
        colorVal = "#007715"
    elif size >18:
        msg = 'EXCELLENT'
        colorVal = "#001fef"
    else:
        pass

    return new_password, msg, colorVal

sz = int(input("Enter size of the password: "))
pas, str, cl = RandPass(sz)
print("Password : ",pas)
print("Strength : ", str)
