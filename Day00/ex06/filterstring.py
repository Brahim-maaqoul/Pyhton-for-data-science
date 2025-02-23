import sys
from ft_filter import ft_filter

def get_words(text: str) -> list:
    str = ''.join(ft_filter(lambda c: c not in "!,\';\".-?", text))
    return str.split()


def main(arg, n):
    try:
        listt = get_words(arg)
        mylist = [x for x in listt if len(x) > int(n)]
        print(mylist)
    except Exception as e:
        print("AssertionError: the arguments are bad")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
    else:
        main(sys.argv[1], sys.argv[2])