def num_generate(n):
    count = 0
    digit = 1
    while n > 0:
        if count < digit:
            yield digit
            n -= 1
            count += 1
        else:
            count = 0
            digit += 1


if __name__ == '__main__':
    for digit in num_generate(int(input())):
        print(digit, end='')
