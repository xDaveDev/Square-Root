from decimal import Decimal, getcontext
import os
import sys
# u wont need to install anything because these are standart libraries


def square_root(initial, times, input):
    a = initial / 2
    b = a * 2 / a
    c = 0

    for c in range(times):
        a = (b + a) / 2
        b = initial / a

    if input < 10000:
        if input > wrap:
            for i in range(0, int(getcontext().prec), wrap):
                print(str(a)[i:i + wrap], end='\n')
        else:
            print(a)
    else:
        print('The answer is in the Result.txt file')
        result = open('Result.txt', 'w')
        result.write(str(a))


Colors = {
    "green": '\u001b' + "[32;1m",
    "blue": "\u001b[34;1m",
    "yellow": "\u001b[33;1m",
}


def logo(text):
    for color in Colors:
        text = text.replace(f"[[{color}]]", Colors[color])
    return text


Logo = open("Logo.txt", "r")
asci = "".join(Logo.readlines())
wrap = 80
while True:
    os.system("cls")
    print(logo(asci))
    number = Decimal(input('From which number do you want to take the square root?: '))
    times = int(input(
        f'How many decimal places should be calculated? (Much more than 100.000 can cause to be inaccurate)\n'))
    getcontext().prec = times + 1
    reps = 21
    square_root(number, reps, times)
    while True:
        again = str(input('Again? "y" for yes and "n" for no:\n (It will clear the console)\n'))
        if again != "y":
            if again != "n":
                print('This is not an answer')
            else:
                sys.exit()
        else:
            break
