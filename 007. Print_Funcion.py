def run(n):
    mensaje = ""
    for i in range(n):
        mensaje = mensaje + str(i+1)

    print(mensaje)

if __name__ == '__main__':
    n = int(input())
    run(n)