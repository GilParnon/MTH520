# python_intro.py
"""Python Essentials: Introduction to Python.
<Gil Parnon>
<MTH 520>
<1/15>
"""

if __name__ == "__main__":
    print("Hello, world!")  
    
def sphere_volume(r):
    """Returns the volume of a sphere for a given radius"""
    return (4/3)*3.14159*(r**3)
def isolate(a,b,c,d,e):
    """Spaces out the inputs"""
    print(a,b, sep='     ', end = '     ')
    print(c,d,e)
    return
def first_half(text):
    """Returns half of the text, rounded down"""
    return(text[0:int(len(text)/2)])
def backward(text):
    """"Returns text backwards"""
    return(text[len(text):0:-1]+text[0])
def list_ops():
    """Does some weird list operations as specified by the lab"""
    myList = ["bear", "ant", "cat", "dog"]
    myList.append("eagle")
    myList[2]  = "fox"
    myList.pop(1)
    myList = sorted(myList, reverse = True)
    myList[myList.index('eagle')] = 'hawk'
    myList[-1] +='hunter'
    return myList
def pig_latin(param):
    """Converts a word to pig-latin, with correct casing"""
    vowel = ['a','e','i','o','u']
    if param[0] in vowel:
        param += 'hay'
    elif param[0].islower():
        param = param[1:len(param)]+param[0]+'ay'
    else:
        param = param[1].upper()+param[2:len(param)]+param[0].lower()+'ay'
    return param
def palindrome():
    """Finds the largest palindrome that is the product of 2 numbers of the specified digits
    returns the number and its factors"""
    digits = 3
    num = 0
    for i in range(10**(digits),10**(digits-1),-1):
        for j in range(i,10**(digits-1),-1):
            numTemp = str(j*i)
            if numTemp == numTemp[::-1] and int(numTemp)>num:
                num = int(numTemp)
                numInd = [i,j]
    return num  #, numInd
def alt_harmonic(terms):
    """Calculates the harmonic series to the number of terms specified"""
    return sum([((-1)**(n+1))/n for n in range(1,terms+1,1)])

# print("A sphere of radius 3 has volume ", sphere_volume(3), ".")
# isolate(1,2,3,4,145)
# print(first_half("Hello"))
# print(backward("Goodbye"))
# print(list_ops())
# print(pig_latin('Math'))
# print(pig_latin('math'))
# print(palindrome())
# print(alt_harmonic(500000))