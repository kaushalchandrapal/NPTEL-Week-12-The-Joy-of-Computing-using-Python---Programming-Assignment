s=input()

def string_test(s):
    upp=0
    low=0
    for c in s:
        if c.isupper():
           upp+=1
        elif c.islower():
           low+=1
        else:
           pass
    print (upp,low,end="")
    
string_test(s)