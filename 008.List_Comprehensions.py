def run (x):
    numeros = []
    for i in range(x):
        if i%3 != 0:
            numeros.append(i**2)

    print(numeros)


if __name__ == '__main__':
    x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())

    run(x)