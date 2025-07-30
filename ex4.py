def sumafin(x):
    tl = 0.005

    n = 360
    r = x * ((tl * pow(1 + tl, n)) / (pow(1 + tl, n) - 1))
    sumaf=r*n
    dobanda=sumaf-x
    print(sumaf)
    print(dobanda)


sumafin(50000)
