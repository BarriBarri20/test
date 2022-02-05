def ListToInt(integers):
    strings = [str(integer) for integer in integers]
    a_string = "". join(strings)
    an_integer = int(a_string)
    return an_integer
def subs(s):
    l=[]
    for i in range(0,len(s)):
        for j in range(len(s),0,-1):
            if len(s[i:j])>1:l.append(s[i:j])
    return l

def isPalindrome(s):
    if s[::-1]==s:
        return True
    else :
        return False
def toStr(l):
    b=[]
    for i in str(l):
        b.append(int(i))
    return b
def result(d):
    for i in subs(d):
        if isPalindrome(i):
            return False
    return True
for i in range(int(input())):
    s=list(input())
    x=s[:len(s)-2]
    
    x+=str(int(s[len(s)-2])+int(s[-1]))
        
    print("".join(x))


