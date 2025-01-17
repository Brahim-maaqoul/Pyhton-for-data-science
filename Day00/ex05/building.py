import sys

def getUppers(str) -> int:
    cp = 0
    for i in str:
        if i.isupper():
            cp+=1
    return cp

def getLowers(str) -> int:
    cp = 0
    for i in str:
        if i.islower():
            cp+=1
    return cp

def getSpaces(str) -> int:
    cp = 0
    for i in str:
        if i.isspace():
            cp+=1
    return cp

def getNums(str) -> int:
    cp = 0
    for i in str:
        if i.isnumeric():
            cp+=1
    return cp

def getPunctuatuions(str) -> int:
    cp = 0
    for i in str:
        if i in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"):  
            cp+=1
    return cp

def main(arg):
    print(f"The text contains {len(arg)} characters:")
    print(getUppers(arg), "upper letters")
    print(getLowers(arg), "lower letters")
    print(getPunctuatuions(arg), "punctuation marks")
    print(getSpaces(arg), "spaces")
    print(getNums(arg), "digits")


if __name__ == "__main__":
    main(sys.argv[1])