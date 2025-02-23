import sys

def main(str):
    NESTED_MORSE = {
    " ": "/",
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

    res = ''
    for i in str:
        if i.upper() in NESTED_MORSE : 
            res = res + NESTED_MORSE[i.upper()]
        else :
            print("AssertionError: the arguments are bad")
            return
    print(res)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
    else:
        main(sys.argv[1])