def run (x, y, z, n):
    print(x,y,z,n)

    i = [i for i in range(x+1) if i<=x]
    j = [i for i in range(y+1) if i<=y]
    k = [i for i in range(z+1) if i<=z]
    
    coord = [[[[ele1, ele2, ele3] for ele3 in k if (ele1 + ele2 +ele3)!=n] for ele2 in j] for ele1 in i]

    # for ele1 in i:
    #     for ele2 in j:
    #         for ele3 in k:
    #             if(ele1 + ele2 + ele3) != n:
    #                 c = [ele1, ele2, ele3]
    #                 coord.append(c)
    print(coord)

if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3

    run(x, y, z, n)